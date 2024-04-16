import os , sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

output_file = "RegisterAsObserver.txt"
# Define a custom file-like object to capture the console output
class ConsoleOutput:
    def __init__(self, file):
        self.file = file

    def write(self, message):
        self.file.write(message)

with open(output_file, "w") as f:
    # Redirect the standard output to the custom file-like object
    sys.stdout = ConsoleOutput(f)
    url = 'https://imolympiad.com/'
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(chrome_options)
    driver.get(url)
    driver.maximize_window()
    image_path = os.path.join('X:\pythonProject\ImOlypiadWebsiteTest', 'testimage.jpg')
    wait = WebDriverWait(driver,25)
    try:
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        print('Page loaded successfully')
    except TimeoutError:
        print("Timeout occurred. Page might not have loaded completely.")

    #Register button at top rigth corner(trc)
    register_trc = driver.find_element(By.XPATH, '//a[@href="/register" and @class="nav-link"]')
    register_trc.click()
    print('The register button at the home page works properly and loads to the registration page')
    # For radio button with Option Yes
    try:
        check_box1 = driver.find_element(By.XPATH,'//*[@id="studentTypeYes"]')
        # driver.execute_script("arguments[0].scrollIntoView();", check_box1)
        actions = ActionChains(driver)
        actions.move_to_element(check_box1).perform()
        check_box1.click()
        print('The radio button with option Yes is clickable')
    except:
        print('The radio button with option Yes is not clickable')

    # Student Id Card Picture
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(image_path)
    print('Student id card picture uploaded successfully')

    #For radio button with option No
    # try:
    #     check_box2 = driver.find_element(By.XPATH, '//*[@id="studentTypeNo"]')
    #     ActionChains(driver).move_to_element(check_box2).perform()
    #     check_box2.click()
    #     print('The radio button with option No is clickable')
    # except:
    #     print('The radio button with option No is not clickable')

    # For Student Image
    student_image = driver.find_element(By.ID, 'studentImage')
    student_image.send_keys(image_path)
    print('Student Image uploaded successfully')

    #For text box name
    name = driver.find_element(By.NAME, 'name')
    name.clear()
    name.send_keys('TestName')
    print('Name is successfully ')
    #For Father Name
    Fname= driver.find_element(By.NAME, 'FatherName')
    Fname.clear()
    Fname.send_keys('TestFatherName')
    print('Father name is successfully sent to the text box')
    #For contact number
    ContactNumber = driver.find_element(By.NAME, 'ContactNumber')
    ContactNumber.clear()
    ContactNumber.send_keys('03000000000')
    print('Contact Number is succesfully sent to the text box')
    #For email
    email= driver.find_element(By.NAME, 'email')
    email.clear()
    email.send_keys('Test@gmail.com')
    print('Email is successfully sent to the text box')
    #For cnic
    cnic = driver.find_element(By.NAME, 'cnic')
    cnic.clear()
    cnic.send_keys('1730100000000')
    print('Cnic is successfully sent to the text box')
    #For Register as Observer
    try:
        observer = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'RegisterAsObserver')))
        ActionChains(driver).move_to_element(observer).perform()
        observer.click()
        print('The Observer radio button is clickable')
    except:
        print('The Observer radio button is not clickable')

    # For ambassador
    ambassador = driver.find_element(By.ID, 'ambassador')
    ambassador.clear()
    ambassador.send_keys('TestAmbassador')
    print('Ambassador name is sent successfully')

    #For payment screenshot
    payment_screenshot = driver.find_element(By.ID, 'paymentScreenshot')
    payment_screenshot.send_keys(image_path)
    print('Payment screenshot uploaded successfully')

# driver.quit()
# Reset the standard output to the console
sys.stdout = sys.__stdout__
