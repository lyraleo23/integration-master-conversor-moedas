import requests
import os
from dotenv import load_dotenv

load_dotenv()

class CallMeBot:
    def __init__(self):
        self.__base_url = f'https://api.callmebot.com/whatsapp.php'
        self.__api_key = os.getenv('CALLMEBOT_API_KEY')
        self.__phone_number = os.getenv('PHONE_NUMBER')
        print(self.__phone_number)

    def send_message(self, message):
        url=f'{self.__base_url}?phone={self.__phone_number}&text={message}&apikey={self.__api_key}'
        print(url)
        response = requests.get(
            url=url
        )
        return response.text
