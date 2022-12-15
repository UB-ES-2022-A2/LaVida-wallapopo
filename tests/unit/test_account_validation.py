import base64
import urllib.request
import imaplib
import email

from email.header import decode_header
from itsdangerous import URLSafeTimedSerializer
from resources.accounts import Accounts


def test_generate_confirmation_token(_app):
    with _app.app_context():
        acc = Accounts()
        user_email = 'pepe432@gmail.com'
        token = acc.generate_confirmation_token(user_email)

        # The token has the format xxxx.yyyy.zzzz, this extracts the header which contains the encoded email
        header = token.split('.')[0]
        # Adding extra chars after the header, so it's length is multiple of 4 (required by b64decode).
        # Then, convert the resulting bytes to string.
        decoded_header = base64.b64decode(header + '.xx').decode('utf-8')
        # Extract the email located between quotation marks (").
        resulting_email = decoded_header.split('"', 1)[1].split('"')[0]

        assert resulting_email == user_email


def test_validate_confirmation_token(_app):
    with _app.app_context():
        acc = Accounts()
        user_email = 'pepe432@gmail.com'
        token = acc.generate_confirmation_token(user_email)

        serializer = URLSafeTimedSerializer(_app.config['SECRET_KEY'])
        resulting_email = serializer.loads(token, salt=_app.config['SECURITY_PASSWORD_SALT'], max_age=3600)

        assert resulting_email == user_email


def test_email_received():
    # account credentials
    username = "wallapopodummy@gmail.com"
    password = "wnxoycxqwiwfcrhq"
    # Gmail provider's IMAP server (from https://www.systoolsgroup.com/imap/)
    imap_server = "imap.gmail.com"
    # Create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL(imap_server, 993)
    # Authenticate
    imap.login(username, password)

    status, messages = imap.select("INBOX")
    # number of top emails to fetch
    N = 3
    # total number of emails
    messages = int(messages[0])

    validation_from = ''
    validation_subject = ''
    confirmation_url = ''
    for i in range(messages, messages - N, -1):
        # Fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # Parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # Decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # If it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # Decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)

                if From == "wallapopo.confirmation@gmail.com":
                    validation_from = From
                    validation_subject = subject
                    body = msg.get_payload(decode=True).decode()
                    # Extract URL from email's body
                    confirmation_url = body.split('"', 1)[1].split('"')[0]

    # Close the connection and logout
    imap.close()
    imap.logout()

    assert validation_from == 'wallapopo.confirmation@gmail.com'
    assert validation_subject == 'Test python email'
    assert confirmation_url == 'https://wallapopo-ub.ew.r.appspot.com/#/emailConfirmation/validation_token=' \
                               'IndhbGxhcG9wb2R1bW15QGdtYWlsLmNvbSI.Y5s58A.6VjydlrVYsDUSGr5i8imIA0NmUE'


def test_valid_url(gmail_imap):
    status, messages = gmail_imap.select("INBOX")
    # Number of top emails to fetch and total number of emails
    N = 3
    messages = int(messages[0])
    confirmation_url = ''

    for i in range(messages, messages - N, -1):
        # Fetch the email message by ID
        res, msg = gmail_imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # Parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # Decode email sender
                sender, encoding = decode_header(msg.get("From"))[0]
                if isinstance(sender, bytes):
                    sender = sender.decode(encoding)

                if sender == "wallapopo.confirmation@gmail.com":
                    body = msg.get_payload(decode=True).decode()
                    # Extract URL from email's body
                    confirmation_url = body.split('"', 1)[1].split('"')[0]

    assert confirmation_url != ''

    is_valid_url = urllib.request.urlopen(confirmation_url).getcode()
    assert is_valid_url == 200
