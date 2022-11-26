from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

host2 = 'http://localhost:8080/'
login_page = host2 + '#/login'

options = Options()
# options.add_argument("--window-size=400,800") # small screen
options.add_argument("--start-maximized")  # max screen
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
