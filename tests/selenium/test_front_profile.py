from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base import login_page, driver

def test_check_profile_data():
    # SETUP: LOGIN AS A USER
    base_url = "http://localhost:5000/"
    driver.get(login_page)

    # Get login form fields and submit button
    email_field = driver.find_element(By.ID, 'login_input_emailField')
    pwd_field = driver.find_element(By.ID, 'login_input_pwdField')
    enter_button = driver.find_element(By.ID, 'login_button_enter')

    # Fill the form with valid credentials
    email_field.send_keys('pepe432@gmail.com')
    pwd_field.send_keys('pepe123,.')

    # Submit the form and login
    enter_button.click()

    login_successfully = WebDriverWait(driver, timeout=5).until(
        lambda d: d.find_element(By.ID, "navbar-identifier"))

    assert login_successfully is not None

    # Look for the profile button at the navbar and click it
    dropdown_button = driver.find_element(By.ID, 'navbar-button-profile')
    dropdown_button.click()

    profile_button = driver.find_element(By.ID, 'perfil')
    profile_button.click()

    profile_page = WebDriverWait(driver, timeout=5).until(
        lambda d: d.find_element(By.ID, "Profile"))

    assert profile_page is not None

    # Check for the profile image icon and change button
    profile_img = driver.find_element(By.ID, 'imProfile')
    change_img_button = driver.find_element(By.ID, 'changeImgButton')
    assert profile_img is not None
    assert change_img_button is not None

    # Check for static data (username and email)
    username_label = driver.find_element(By.XPATH, "//div[@id='profile-div-username']//label")
    username_span = driver.find_element(By.XPATH, "//div[@id='profile-div-username']//span")
    assert username_label.text == "Nombre de usuario"
    assert username_span.text == "pepeman"

    email_label = driver.find_element(By.XPATH, "//div[@id='profile-div-email']//label")
    email_span = driver.find_element(By.XPATH, "//div[@id='profile-div-email']//span")
    assert email_label.text == "Email"
    assert email_span.text == "pepe432@gmail.com"

    # Check for editable data (name, surname and birthday plus save button)
    public_info = driver.find_element(By.ID, 'publicInfo')
    name_input = driver.find_element(By.ID, 'input-name')
    surname_input = driver.find_element(By.ID, 'input-surname')
    birthday_input = driver.find_element(By.ID, 'start')
    save_button = driver.find_element(By.ID, 'saveBUtton')

    assert public_info is not None
    assert name_input is not None
    assert surname_input is not None
    assert birthday_input is not None
    assert save_button is not None

    driver.close()
    driver.quit()
