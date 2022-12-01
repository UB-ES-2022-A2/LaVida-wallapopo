from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base import driver, host2


login_page = host2 + '#/login'


def test_make_a_correct_login_filling_with_real_account():

    driver.get(login_page)
    email_field = driver.find_element(By.ID, 'login_input_emailField')
    pwd_field = driver.find_element(By.ID, 'login_input_pwdField')
    enter_button = driver.find_element(By.ID, 'login_button_enter')

    # Fill the fields to make login

    email_field.send_keys('admin123@gmail.com')
    pwd_field.send_keys('admin123@gmail.com')

    # Click "enter" to login
    enter_button.click()
    login_exitoso = WebDriverWait(driver, timeout=2).until(lambda d: d.find_element(By.ID, "navigationBar_div_addProduct"))

    # Si el login es exitoso se hara display a un nuevo elemento

    assert login_exitoso is not None

test_make_a_correct_login_filling_with_real_account()
