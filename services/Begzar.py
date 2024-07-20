from bs4 import BeautifulSoup
import requests

def GetGetBegzarHandler(url):
    prefix = 'https://begzar.ir'
    response = requests.get(prefix)

    soup = BeautifulSoup(response.text, 'html.parser')
    form = soup.find('form', {'title': 'با بگذر میتونی همه سایتهایی که ایران را تحریم کردن باز کنی.'})

    form_action = prefix
    input_name = form.find('input', {'name': 'domain_name'}).get('name')
    
    post_data = {
        input_name: url,
        'search_domain': 'بررسی کن'
    }

    response = requests.post(form_action, data=post_data)
    if response.status_code == 200:
        result_soup = BeautifulSoup(response.text, 'html.parser')

        message_box = result_soup.find("p", {"class": "messagebox"})
        if message_box:
            isSuccess = message_box.text.strip() == " تحریمی است و در \"بگذر\" پشتیبانی می شود !".strip()
            return { 'IsSuccess': isSuccess}