from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

host = 'https://firm-affinity-366616.ew.r.appspot.com/'
host2 = 'http://localhost:8080/'
login_page = host2 + '#/login'


def set_webpage(url):
    # Set Page
    options = Options()
    # options.add_argument("--window-size=400,800") # small screen
    options.add_argument("--start-maximized")  # max screen
    # options.add_argument("--headless") # do not open browser

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver.get(url)


def test_make_a_correct_login_filling_with_real_account():
    options = Options()
    # options.add_argument("--window-size=400,800") # small screen
    options.add_argument("--start-maximized")  # max screen
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(login_page)
    email_field = driver.find_element(By.ID, 'login_input_emailField')
    pwd_field = driver.find_element(By.ID, 'login_input_pwdField')
    enter_button = driver.find_element(By.ID, 'login_button_enter')


    # Fill the fields to make login


    email_field.send_keys('admin123@gmail.com')
    pwd_field.send_keys('admin123@gmail.com')

    # Click "enter" to login
    enter_button.click()
    g = host2 + '#/'
    print("JAJAJ",driver.current_url)
    assert driver.current_url is g

driver = set_webpage(login_page)

test_make_a_correct_login_filling_with_real_account()
