from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
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
    staleElement = True
    while(staleElement):
        try:
            sleep(2)
            user = wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath)))
            user.click()
            staleElement = False
        except Exception:
            staleElement = True
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    print("Message send successfully.")
        
    
if __name__ == "__main__":

    print("Web Page Open")
    # Let us login and Scan
    whatsapp_login()
    
    with open('data_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("Column names are "+ ", ".join(row))
                line_count += 1
            else:
                send_message(row[0],row[1],int(row[2]))
                line_count += 1
        print('Processed {} lines.'.format(line_count))
    
    sleep(10)
    driver.close() # Close the Open tab
    driver.quit()