from time import sleep

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from base import driver, host2
from selenium.webdriver.support import expected_conditions as EC

login_page = host2 + '#/login'


def login():
    driver.get(login_page)
    email_field = driver.find_element(By.ID, 'login_input_emailField')
    pwd_field = driver.find_element(By.ID, 'login_input_pwdField')
    enter_button = driver.find_element(By.ID, 'login_button_enter')

    # Fill the fields to make login

    email_field.send_keys('admin123@gmail.com')
    pwd_field.send_keys('admin123@gmail.com')

    # Click "enter" to login
    enter_button.click()
    login_exitoso = WebDriverWait(driver, timeout=3).until(
        lambda d: d.find_element(By.ID, "navigationBar_div_addProduct"))

    # Si el login es exitoso se hara display a un nuevo elemento

    assert login_exitoso is not None
    return driver


def add_product():
    login()
    add_product_page = host2 + '#/catalog/add'
    driver.get(add_product_page)

    # Get all elements in page
    product_title_field = driver.find_element(By.ID, 'input-1')
    product_category = Select(driver.find_element(By.NAME, 'categoryId'))
    product_price = driver.find_element(By.ID, 'input-2')
    product_state = Select(driver.find_element(By.ID, 'productStateId'))
    product_description = driver.find_element(By.ID, 'productDescription')
    product_add_photo = driver.find_element(By.ID, 'addProduct_input_subirProducto')
    product_uploadProduct_button = driver.find_element(By.ID, 'addProduct_button_subirProducto')

    # Fill info to upload a product
    product_title_field.send_keys('Monopolio')
    product_category.select_by_visible_text('Motos')
    product_price.send_keys('5')
    product_state.select_by_visible_text('Nuevo')
    product_description.send_keys("Un monopolio con tema de motos")
    product_add_photo.send_keys("C:/Users/migue/Downloads/lena.jpg")
    product_uploadProduct_button.click()
    alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    print(alert_text)
    sleep(2)
    assert alert_text is not None


add_product()
