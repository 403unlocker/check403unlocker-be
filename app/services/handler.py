import json
from typing import Union
from urllib.request import urlopen
from bs4 import BeautifulSoup
from httpx import AsyncClient



class Handler:
    def __init__(self,httpx_client:AsyncClient) -> None:
        self.httpx_client = httpx_client
        

    async def get_shecan(self,url:str) -> bool:
        try:
            url = url.replace("https://", "")
            url = f'https://shecan.ir/?url=https%3A%2F%2F{url}#report'

            response = await self.httpx_client.post(url)
            if response.status_code != 200:
                return False
            result_soup = BeautifulSoup(response.text, 'html.parser')
            message_box = result_soup.find("p", {"class": "messagebox"})
            if message_box:
                isSuccess = message_box.text == " این سایت ایران را تحریم کرده است و شکن آن را پشتیبانی می‌کند."
                return isSuccess
        except:
            return False
    

    async def get_vanilla(self, url: str) -> bool:
        try:
            url = f'https://vanillapp.ir/api/check/?target={url}'
            response = await self.httpx_client.get(url)
            if response.status_code != 200:
                return False
            data = response.json()
            return data['status']
        except:
            return False

    async def get_begzar(self, url: str) -> bool:
        try:
            prefix = 'https://begzar.ir'
        
            response = await self.httpx_client.get(prefix)
            if response.status_code != 200:
                return False

            soup = BeautifulSoup(response.text, 'html.parser')
            form = soup.find('form', {'title': 'با بگذر میتونی همه سایتهایی که ایران را تحریم کردن باز کنی.'})

            if not form:
                return  False

            form_action = prefix
            input_name = form.find('input', {'name': 'domain_name'}).get('name')

            post_data = {
                    input_name: f"https://{url}",
                    'search_domain': 'بررسی کن'
                }

            response = await self.httpx_client.post(form_action, data=post_data)
            if response.status_code != 200:
                return {'IsSuccess': False, 'Error': 'Failed to submit form'}

            result_soup = BeautifulSoup(response.text, 'html.parser')
            message_box = result_soup.find("p", {"class": "messagebox"})

            if message_box:
                is_success = message_box.text.strip() == "تحریمی است و در \"بگذر\" پشتیبانی می شود !".strip()
                return is_success
            
            return False
        except:
            return False
    

    async def get_anti403(self,url:str) -> bool:
        try:
            data = urlopen(f'https://api.anti403.ir/api/search-filter?url={url}').read()
            parseToJson = json.loads(data)
            return parseToJson["result"]["support"]
        except:
            return False
    
    
    async def get_darzgir(self, url: str) -> bool:
        try:
            url = f'https://api.darzg.ir/v1/domains/{url}/'

            response = await self.httpx_client.get(url)
            if response.status_code == 200:
                data = response.json()
                return data['message'] == 'domain is supported!'

            return False
        except:
            return False