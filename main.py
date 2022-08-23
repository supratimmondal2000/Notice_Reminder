from selenium import webdriver
import os
import smtplib
import time
from email.message import EmailMessage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime

while True:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options = chrome_options)

    
    driver.get("https://nitdgp.ac.in/")
    driver.implicitly_wait(10)
    dates = driver.find_elements(By.XPATH, "//div[@class='date']")
    links = driver.find_elements(By.XPATH, "//a[@target='_blank']")
    todayDate = datetime.today()
    print(todayDate)
    for date, link in zip(dates, links):
        tday = date.text
        print(tday)
        #today1 = tday.split(' ')
        str="20"
        if tday[1:2] == '\n':
            str = str + tday[6:8]
            str = str + '-'
            if tday[2:5] == 'JAN':
                str = str + '01'
            if tday[2:5] == 'FEB':
                str = str + '02'
            if tday[2:5] == 'MAR':
                str = str + '03'
            if (tday[2:5] == 'APR'):
                str = str + '04'
            if (tday[2:5] == 'MAY'):
                str = str + '05'
            if (tday[2:5] == 'JUN'):
                str = str + '06'
            if (tday[2:5] == 'JUL'):
                str = str + '07'
            if (tday[2:5] == 'AUG'):
                str = str + '08'
            if (tday[2:5] == 'SEP'):
                str = str + '09'
            if (tday[2:5] == 'OCT'):
                str = str + '10'
            if (tday[2:5] == 'NOV'):
                str = str + '11'

            if (tday[2:5] == 'DEC'):
                str = str + '12'

            str = str + '-'
            str = str + tday[0:1]


        else:
            str = str + tday[7:9]
            str = str + '-'
            if tday[3:6] == 'JAN':
                str = str + '1'
            if tday[3:6] == 'FEB':
                str = str + '2'
            if tday[3:6] == 'MAR':
                str = str + '3'
            if (tday[3:6] == 'APR'):
                str = str + '4'
            if (tday[3:6] == 'MAY'):
                str = str + '5'
            if (tday[3:6] == 'JUN'):
                str = str + '6'
            if (tday[3:6] == 'JUL'):
                str = str + '7'
            if (tday[3:6] == 'AUG'):
                str = str + '8'
            if (tday[3:6] == 'SEP'):
                str = str + '9'
            if (tday[3:6] == 'OCT'):
                str = str + '10'
            if (tday[3:6] == 'NOV'):
                str = str + '11'

            if (tday[3:5] == 'DEC'):
                str = str + '12'

            str = str + '-'
            str = str + tday[0:2]

        print(str)
        temp = todayDate.strftime('%y-%m-%d')
        #str1= '2021-10-28'
        if  temp == str:
            data = link.text

            if (data.find('Scholarship') != -1 or data.find('UG') != -1 or
                    (data.find('Payment') != -1 and data.find('UG') != -1)
                    or (data.find('Registration') != -1 and data.find('UG') != -1)
                    or data.find('COVID-19') != -1):
                print(link.get_attribute('href'))
                msg = EmailMessage()
                msg['Subject'] = link.text
                msg['From'] = 'Remainder Team'
                msg['To'] = 'arindamparia321@gmail.com'
                msg.set_content(link.get_attribute("href"))
                server1 = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server1.login("collegeremainder@gmail.com", "Nitdgp@9064")
                server1.send_message(msg)
                server1.quit()
            else:
                print("not Found")
        else:
            print("continue")
            continue
    time.sleep(86400)