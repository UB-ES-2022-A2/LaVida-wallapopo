import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def options():
    options = Options()
    options.add_argument("--start-maximized")  # max screen
    yield options


@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver

