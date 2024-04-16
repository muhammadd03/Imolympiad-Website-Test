import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://imolympiad.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
output_file = "AboutPage.txt"
# Define a custom file-like object to capture the console output
class ConsoleOutput:
    def __init__(self, file):
        self.file = file

    def write(self, message):
        self.file.write(message)

with open(output_file, "w") as f:
    # Redirect the standard output to the custom file-like object
    sys.stdout = ConsoleOutput(f)

    wait = WebDriverWait(driver,10)
    try:
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        print('Page loaded successfully')
    except TimeoutError:
        print("Timeout occurred. Page might not have loaded completely.")

    about = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
    # //*[@id="navbarSupportedContent"]/ul/li[2]/a
    about.click()
    print('Successfully loaded to About page')
    # driver.implicitly_wait(5)
    # <a class="nav-link" href="#about">About</a>
    # driver.execute_script()
    #register button on about page(ap)
    try:
        register_ap = driver.find_element(By.XPATH, '//*[@id="about"]/div/div[2]/div[2]/div/a')
        actions = ActionChains(driver)
        actions.move_to_element(register_ap).perform()
        register_ap.click()
        print('The register button on the about page is clickable')
    except:
        print('The register button on the about page is not clickable')

driver.quit()
sys.stdout = sys.__stdout__
