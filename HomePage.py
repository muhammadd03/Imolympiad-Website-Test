import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
url = 'https://imolympiad.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
output_file = "HomePage.txt"
# Define a custom file-like object to capture the console output
class ConsoleOutput:
    def __init__(self, file):
        self.file = file

    def write(self, message):
        self.file.write(message)

with open(output_file, "w") as f:
    # Redirect the standard output to the custom file-like object
    sys.stdout = ConsoleOutput(f)
    try:
        WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        print('Page loaded successfully')
    except TimeoutError:
        print("Timeout occurred. Page might not have loaded completely.")
    # # Register button at top rigth corner(trc)
    register_trc = driver.find_element(By.XPATH, '//a[@href="/register" and @class="nav-link"]')
    register_trc.click()
    driver.implicitly_wait(5)
    print('The register button at the home page works properly and loads to the registration page')
    #Now getting back to the home page and going for the register button ate the end of the page
    back_to_home = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[1]/a')
    back_to_home.click()
    print('Now the driver is back at the home page')
    try:
        WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        print('Page loaded successfully')
    except TimeoutError:
        print("Timeout occurred. Page might not have loaded completely.")
    #Register button in the end of the page
    try:
        register_end =WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/register" and @class="boxed-btn3 mt-3 wow fadeInUp"]')))
        actions = ActionChains(driver)
        actions.move_to_element(register_end).perform()
        register_end.click()
        print('The register button at the home page works properly and loads to the registration page')
    except:
        print('The register button at the end of the page is not clickable')

driver.quit()
sys.stdout = sys.__stdout__
