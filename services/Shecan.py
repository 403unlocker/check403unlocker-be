from time import sleep
from bs4 import BeautifulSoup
import requests



def GetShecanHandler(url):
    url = url.replace("https://", "")
    url = f'https://shecan.ir/?url=https%3A%2F%2F{url}#report'

    response = requests.post(url)
    if response.status_code == 200:
        print("Form submitted successfully!")
        result_soup = BeautifulSoup(response.text, 'html.parser')
        message_box = result_soup.find("p", {"class": "messagebox"})
        if message_box:
            isSuccess = message_box.text == " این سایت ایران را تحریم کرده است و شکن آن را پشتیبانی می‌کند."
            return { 'IsSuccess': isSuccess}