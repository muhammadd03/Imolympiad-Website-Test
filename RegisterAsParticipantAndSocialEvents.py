import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Define the file name where you want to redirect the console output
output_file = "RegisterAsParticipantAndSocialEvents.txt"

# Define a custom file-like object to capture the console output
class ConsoleOutput:
    def __init__(self, file):
        self.file = file

    def write(self, message):
        self.file.write(message)

# Open the file in write mode
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

    #For register as participant and social event
    try:
        participantandsocialevent = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[1]/div[3]/input')))
        # participant = wait.until(EC.element_to_be_clickable(By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[1]/div[3]/input'))
        ActionChains(driver).move_to_element(participantandsocialevent).perform()
        participantandsocialevent.click()
        print('The Participant and social event button is clickable')
    except:
        print('The Participant and social event radio button is not clickable')
    #For Futsal
    futsal = driver.find_element(By.ID, 'Futsal')
    ActionChains(driver).move_to_element(futsal).perform()
    futsal.click()
    print('The Futsal radio button is clickable')
    futsalplayers = driver.find_element(By.ID, 'FutsalPlayers')
    futsalplayers.clear()
    futsalplayers.send_keys('7')
    print('Player numbers are successfully sent to the Futsal Player text box')
    for futsal_player_number in range(1, 8):
        #For Player Type Yes
        playertype_yes = driver.find_element(By.ID, f'playerTypeYes{futsal_player_number}')
        ActionChains(driver).move_to_element(playertype_yes).perform()
        playertype_yes.click()
        #For Player is a student of Imsciences
        futsal_player_ims_std = driver.find_element(By.ID, f'playerID{futsal_player_number}')
        futsal_player_ims_std.send_keys(image_path)
        #For Player Type No
        playertype_no = driver.find_element(By.ID, f'playerTypeNo{futsal_player_number}')
        ActionChains(driver).move_to_element(playertype_no).perform()
        playertype_no.click()
        # For Futsal Player Image
        futsal_player_img = driver.find_element(By.ID, f'playerImage{futsal_player_number}')
        futsal_player_img.send_keys(image_path)
        #For Player Name
        player_name = driver.find_element(By.ID, f'playerName{futsal_player_number}')
        player_name.clear()
        player_name.send_keys('Test')
        #For Player Contact
        player_contact = driver.find_element(By.ID, f'playerContact{futsal_player_number}')
        player_contact.clear()
        player_contact.send_keys('03000000000')
        #For Player CNIC
        player_cnic = driver.find_element(By.ID, f'playerCnic{futsal_player_number}')
        player_cnic.clear()
        player_cnic.send_keys('1730100000000')
        # For futsal player cnic image
        futsal_player_cnic_img = driver.find_element(By.ID, f'playerCnicImg{futsal_player_number}')
        futsal_player_cnic_img.send_keys(image_path)

        #For Player wants to attend the social event
        player_attend_social_event = driver.find_element(By.ID, f'playerAttendSocialEventYes{futsal_player_number}')
        ActionChains(driver).move_to_element(player_attend_social_event).perform()
        player_attend_social_event.click()
    print("All the Futsal Player's details are sent and all the functionalitites are working correctly correctly ")

    # For Basktelball
    basketball = driver.find_element(By.ID, 'Basketball')
    ActionChains(driver).move_to_element(basketball).perform()
    basketball.click()
    print('The Basketball radio button is clickable')
    basketball_player = driver.find_element(By.NAME, 'BasketballPlayers')
    basketball_player.clear()
    basketball_player.send_keys(7)
    print('Player numbers are succesfully sent to the Basketball player text box')
    for basketball_player_number in range(1, 8):
            #For Player Type Yes
            playertype_yes = driver.find_element(By.ID, f'basketballPlayerTypeYes{basketball_player_number}')
            ActionChains(driver).move_to_element(playertype_yes).perform()
            playertype_yes.click()
            # For Basketball player is an Imsciences student
            basketball_player_image_ims_std = driver.find_element(By.ID, f'basketballPlayerID{basketball_player_number}')
            basketball_player_image_ims_std.send_keys(image_path)
            #For Player Type No
            playertype_no = driver.find_element(By.ID, f'basketballPlayerTypeNo{basketball_player_number}')
            ActionChains(driver).move_to_element(playertype_no).perform()
            playertype_no.click()
            # For basketball player image
            basketball_player_img = driver.find_element(By.ID, f'basketballPlayerImage{basketball_player_number}')
            basketball_player_img.send_keys(image_path)
            #For Player Name
            player_name = driver.find_element(By.ID, f'basketballPlayerName{basketball_player_number}')
            player_name.clear()
            player_name.send_keys('Test')

            #For Player Contact
            player_contact = driver.find_element(By.ID, f'basketballPlayerContact{basketball_player_number}')
            player_contact.clear()
            player_contact.send_keys('03000000000')

            #For Player CNIC
            player_cnic = driver.find_element(By.ID, f'basketballPlayerCnic{basketball_player_number}')
            player_cnic.clear()
            player_cnic.send_keys('1730100000000')

            #For player cnic image
            basketball_player_cnic_img = driver.find_element(By.ID, f'basketballPlayerCnicImg{basketball_player_number}')
            basketball_player_cnic_img.send_keys(image_path)

            #For Player wants to attend the social event
            player_attend_social_event = driver.find_element(By.ID, f'BasketballplayerAttendSocialEventYes{basketball_player_number}')
            ActionChains(driver).move_to_element(player_attend_social_event).perform()
            player_attend_social_event.click()
    print("All the Basketball Player's details are sent and all the functionalities are working correctly ")

    # For Badminton
    badminton = driver.find_element(By.ID, 'Badminton')
    ActionChains(driver).move_to_element(badminton).perform()
    badminton.click()
    print('The Badminton radio button is clickable')
    # For badminton second player
    double = driver.find_element(By.ID, 'double')
    ActionChains(driver).move_to_element(double).perform()
    double.click()
    # For second player type yes
    badminton_second_player_type_yes= driver.find_element(By.ID,'badmintonSecondPlayerTypeYes')
    ActionChains(driver).move_to_element(badminton_second_player_type_yes).perform()
    badminton_second_player_type_yes.click()
    # For second player type no
    badminton_second_player_type_no= driver.find_element(By.ID,'badmintonSecondPlayerTypeNo')
    ActionChains(driver).move_to_element(badminton_second_player_type_no).perform()
    badminton_second_player_type_no.click()
    # For second player name
    badminton_second_player_name = driver.find_element(By.ID,'badmintonSecondPlayerName')
    badminton_second_player_name.clear()
    badminton_second_player_name.send_keys('Test')
    # For second player contact number
    badminton_second_player_contact = driver.find_element(By.ID, 'badmintonSecondPlayerContact')
    badminton_second_player_contact.clear()
    badminton_second_player_contact.send_keys('03000000000')
    # For second player cnic
    badminton_second_player_cnic = driver.find_element(By.ID, 'badmintonSecondPlayerCnic')
    badminton_second_player_cnic.clear()
    badminton_second_player_cnic.send_keys('1730100000000')
    # For second player cnic image
    badminton_second_player_cnic_img = driver.find_element(By.ID, 'badmintonSecondPlayerCnicImage')
    badminton_second_player_cnic_img.send_keys(image_path)
    # For Second player social event
    # For yes
    badminton_second_player_social_event_yes = driver.find_element(By.ID, 'badmintonSecondPlayerAttendSocialEventYes')
    ActionChains(driver).move_to_element(badminton_second_player_social_event_yes).perform()
    badminton_second_player_social_event_yes.click()
    # For no
    badminton_second_player_social_event_no = driver.find_element(By.ID, 'badmintonSecondPlayerAttendSocialEventNo')
    ActionChains(driver).move_to_element(badminton_second_player_social_event_no).perform()
    badminton_second_player_social_event_no.click()
    print("The Badminton second player radio button is clickable and all the functionalities are correctly working")
    # For Table Tennis
    tabletennis = driver.find_element(By.ID, 'TableTennis')
    actions = ActionChains(driver)
    ActionChains(driver).move_to_element(tabletennis).perform()
    tabletennis.click()
    print('The Table Tennis radio button is clickable')
    # For Board Games
    boardgames = driver.find_element(By.ID, 'BoardGames')
    ActionChains(driver).move_to_element(boardgames).perform()
    boardgames.click()
    print('The Board games radio button is clickable')
    # For ludo
    ludo = driver.find_element(By.ID, 'Ludo')
    ActionChains(driver).move_to_element(ludo).perform()
    ludo.click()
    print('The Ludo radio button is clickable')
    # For Chess
    chess = driver.find_element(By.ID, 'Chess')
    ActionChains(driver).move_to_element(chess).perform()
    chess.click()
    print('The Chess radio button is clickable')
    # For Carrom
    carrom = driver.find_element(By.ID, 'Carrom')
    ActionChains(driver).move_to_element(carrom).perform()
    carrom.click()
    print('The Carrom radio button is clickable')
    # For Egaming
    egaming = driver.find_element(By.ID, 'EGaming')
    ActionChains(driver).move_to_element(egaming).perform()
    egaming.click()
    print('The E-Gaming radio button is clickable')
    # For tekken
    tekken = driver.find_element(By.ID, 'Tekken')
    ActionChains(driver).move_to_element(tekken).perform()
    tekken.click()
    print('The Tekken radio button is clickable')
    # For Fifa
    fifa = driver.find_element(By.ID, 'Fifa')
    ActionChains(driver).move_to_element(fifa).perform()
    fifa.click()
    print('The Fifa radio button is clickable')
    #For parliamentary summit
    parliamentarysummit = driver.find_element(By.ID, 'ParliamentarySummit')
    ActionChains(driver).move_to_element(parliamentarysummit).perform()
    parliamentarysummit.click()
    print('The Parliamentary summit radio button is clickable')
    # For leader of the house
    # For yes
    leader_of_the_house_yes= driver.find_element(By.ID, 'LeaderOfHouseYes')
    ActionChains(driver).move_to_element(leader_of_the_house_yes).perform()
    leader_of_the_house_yes.click()
    print('The option Yes radio button for the leader of house is clickable')
    # For no
    leader_of_the_house_no= driver.find_element(By.ID, 'LeaderOfHouseNo')
    ActionChains(driver).move_to_element(leader_of_the_house_no).perform()
    leader_of_the_house_no.click()
    print('The option No radio button for the leader of house is clickable')
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
sys.stdout = sys.__stdout__
