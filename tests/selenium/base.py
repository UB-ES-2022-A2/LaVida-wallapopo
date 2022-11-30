from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import TimeoutException

host2 = 'http://localhost:8080/'
login_page = host2 + '#/login'

options = Options()
options.add_argument("--window-size=400,800")

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)