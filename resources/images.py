from werkzeug.utils import secure_filename
from flask import request
import os
from lock import lock
from flask_restful import Resource
from sqlalchemy import exc
from http import HTTPStatus
from google.cloud import storage

from db import db
from models.accounts import AccountsModel
from models.products import ProductsModel


class ImagesProducts(Resource):

    def post(self, id):
        with lock.lock:
            """Process the uploaded file and upload it to Google Cloud Storage."""
            uploaded_files = request.files.getlist('file')

            if not uploaded_files:
                return 'No file uploaded.', 400

            # Create a Cloud Storage client.
            gcs = storage.Client.from_service_account_json('wallapopo-ub-d41a3647fa63.json')

            # Get the bucket that the file will be uploaded to.
            bucket = gcs.get_bucket('wallapopo-img')

            # Create a new blob and upload the file's content.
            product = ProductsModel.get_by_id(id)
            for file in uploaded_files:
                blob = bucket.blob(f"product/{id}/{file.filename}")

                blob.upload_from_string(
                    file.read(),
                    content_type=file.content_type
                )
                product.images(blob.public_url)

            try:
                product.save_to_db()
                return {'message': 'Images uploaded successfully'}
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'Error while uploading images'}, HTTPStatus.INTERNAL_SERVER_ERROR


class ImagesUsers(Resource):

    def post(self, email):
        with lock.lock:
            """Process the uploaded file and upload it to Google Cloud Storage."""
            uploaded_file = request.files['file']

            if not uploaded_file:
                return 'No file uploaded.', 400

            # Create a Cloud Storage client.
            gcs = storage.Client.from_service_account_json('wallapopo-ub-d41a3647fa63.json')

            # Get the bucket that the file will be uploaded to.
            bucket = gcs.get_bucket('wallapopo-img')

            # Create a new blob and upload the file's content.
            user = AccountsModel.get_by_email(email)
            blob = bucket.blob(f"profile/{email}/{uploaded_file.filename}")

            blob.upload_from_string(
                uploaded_file.read(),
                content_type=uploaded_file.content_type
            )
            user.images(blob.public_url)
            try:
                user.save_to_db()
                return {'message': 'Images uploaded successfully'}
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'Error while uploading images'}, HTTPStatus.INTERNAL_SERVER_ERROR

