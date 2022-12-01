from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException


host = 'http://127.0.0.1:5000/'
login_page = host + '#/login'
register_page = host + '#/register'
add_product_page = host + '#/catalog/add'
profile_page = host + '#/profile'


options = Options()
# options.add_argument("--window-size=400,800") # small screen
options.add_argument("--start-maximized")  # max screen
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # Instance of web



