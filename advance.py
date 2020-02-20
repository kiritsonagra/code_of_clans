from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

driver = None
Link = "https://web.whatsapp.com/"
wait = None

def whatsapp_login():
    global wait, driver, Link
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 600)
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")

def send_message(name,msg,count):
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    flag = True
    while(flag):
        try:
            sleep(2)
            user = wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath)))
            user.click()
            flag = False
        except Exception:
            flag = True
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    print("Message send successfully.")

if __name__ == "__main__":

    name = input('Enter the name of user or group : ')
    msg = input('Enter the message : ')
    count = int(input('Enter the count : '))
    # Let us login and Scan
    print("Now, Web Page Open")
    whatsapp_login()
    send_message(name,msg,count)

    sleep(10)
    driver.close()
    driver.quit()
