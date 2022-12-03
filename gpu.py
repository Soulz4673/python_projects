#basic scapper 
#
#
#https://www.youtube.com/watch?v=Bg9r_yLk7VY
#
#install pip install requests bs4
#pull data from website
import requests
from bs4 import BeautifulSoup
#enable email notification
import smtplib
import time
URL = 'https://www.amazon.com/NVIDIA-GeForce-Founders-Graphics-GDDR6X/dp/B0BJFRT43X/ref=sr_1_3?crid=2XVPH6F933KCM&keywords=4090&qid=1670039089&sprefix=4090%2Caps%2C144&sr=8-3&ufe=app_do%3Aamzn1.fos.17f26c18-b61b-4ce9-8a28-de351f41cffb'
# Changed the user agent info Chrome and Safri
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{100.0.0.0}}Safari/100.10'}

def check_price():
    page = requests.get(URL, headers = headers)


    soup = BeautifulSoup(page.conent,'html.parser')

    ##print(soup.prettify())

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price< 1.500):
        send_mail()
    #print(converted_price)
    #print(title.strip())



#https://docs.python.org/3/library/smtplib.html
def send_mail():
    server = smtplib.SMTP('smtp.@gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #email and two setp authorization
    server.login('------@gmail','sahdfuja')

    subject = 'Price fell'
    body = 'Check the amazon link https://www.amazon.com/NVIDIA-GeForce-Founders-Graphics-GDDR6X/dp/B0BJFRT43X/ref=sr_1_3?crid=2XVPH6F933KCM&keywords=4090&qid=1670039089&sprefix=4090%2Caps%2C144&sr=8-3&ufe=app_do%3Aamzn1.fos.17f26c18-b61b-4ce9-8a28-de351f41cffb'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '----@gmail.com'
        'asdf@gmail.com'
        msg
    )
    print('Email been sent')
    
    server.quit()

while(True):
    check_price()
    #checks 60 seconds
    time.sleep(60)

