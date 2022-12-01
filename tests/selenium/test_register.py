from selenium.webdriver.common.by import By

from base import driver, host, register_page


def test_register_with_valid_information():
    driver.get(register_page)
    username = driver.find_element(By.ID, 'inputName')
    email = driver.find_element(By.ID, 'inputEmail')
    psw = driver.find_element(By.ID, 'inputPassword')
    psw2 = driver.find_element(By.ID, 'inputPassword2')
    checkbox = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/p/div[5]/div/label')
    register = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/button[1]')

    # Valores correctos para comprobar
    username.send_keys('Este es mi nombre')
    email.send_keys('abcde@abcde.com')
    psw.send_keys('mamamamaa1!')
    psw2.send_keys('mamamamaa1!')
    checkbox.click()

    # Comprobamos boton esta enabled
    result = register.is_enabled()
    assert result is True


def test_register_with_invalid_info():
    driver.get(register_page)
    username = driver.find_element(By.ID, 'inputName')
    email = driver.find_element(By.ID, 'inputEmail')
    psw = driver.find_element(By.ID, 'inputPassword')
    psw2 = driver.find_element(By.ID, 'inputPassword2')
    checkbox = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/p/div[5]/div/label')
    register = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/button[1]')

    # Introducimos valores incorrectos
    username.send_keys('Este es mi nombre')
    email.send_keys('Mi correo')
    psw.send_keys('Mi contraseña')
    psw2.send_keys('Mi contraseña2')
    checkbox.click()

    # Comprobamos boton esta disabled
    result = register.is_enabled()
    assert result is False

def test_register_button_with_empty_data():
        driver.get(register_page)
        username = driver.find_element(By.ID, 'inputName')
        email = driver.find_element(By.ID, 'inputEmail')
        psw = driver.find_element(By.ID, 'inputPassword')
        psw2 = driver.find_element(By.ID, 'inputPassword2')
        checkbox = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/p/div[5]/div/label')
        register = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/button[1]')


        checkbox.click()

        # Comprobamos boton esta disabled
        result = register.is_enabled()
        assert result is False