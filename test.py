from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 1 зайти на главную страницу
# 2 выбрать поле Username
# 3 ввести standard_user
# 4 выбрать поле Password
# 5 ввести secret_sauce
# 6 нажать кнопку Login

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

def open_page(driver, URL):
    driver.get(URL)

def get_element_by_id(driver, locator):
   return driver.find_element(By.ID, locator)

def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()

def element_send_keys(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)

def login(driver, name, password):
    element_send_keys(driver, 'user-name', name)
    element_send_keys(driver, 'password', password)
    element_click(driver, 'login-button')

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

driver = get_driver()
open_page(driver, URL)
login(driver=driver, name=LOGIN, password=PASSWORD)

driver.quit()