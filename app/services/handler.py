from typing import Union
from bs4 import BeautifulSoup
from httpx import AsyncClient



class Handler:

    def __init__(self,httpx_client:AsyncClient) -> None:
        self.httpx_client = httpx_client
        

    async def get_shecan(self,url:str) -> Union[bool,str]:
        url = url.replace("https://", "")
        url = f'https://shecan.ir/?url=https%3A%2F%2F{url}#report'

        response = await self.httpx_client.post(url)
        if response.status_code == 200:
            result_soup = BeautifulSoup(response.text, 'html.parser')
            message_box = result_soup.find("p", {"class": "messagebox"})
            if message_box:
                isSuccess = message_box.text == " این سایت ایران را تحریم کرده است و شکن آن را پشتیبانی می‌کند."
                return isSuccess
            

    async def get_vanilla(self, url: str) -> bool:
        url = f'https://vanillapp.ir/api/check/?target={url}'
        
        response = await self.httpx_client.get(url=url)
        if response.status_code == 200:
                data = response.json()
                return data.get('status', False)
        return False
    

    async def get_begzar(self, url: str) -> bool:
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
                input_name: url,
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
    


    async def get_anti403(self,url:str) -> bool:
        url = f'https://api.anti403.ir/api/search-filter?url={url}'

        response = await self.httpx_client.get(url=url)
        if response.status_code == 200:
                data = response.json()
                return data.get('status', False)
        return False
    