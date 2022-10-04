import dataclasses
import html
import datetime
from datetime import date


import requests
from zodiac_sign import get_zodiac_sign
from bs4 import BeautifulSoup


# url = 'https://horoscopes.rambler.ru/taurus/' 


# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.find(itemprop='articleBody'))


class ParseHoroscope():

    def __init__(self, date):

        date = None
        zodiac_sign = None
    
    
    def get_zodiac_sign(self, date):

        date = datetime.fromisoformat(date)
        self.zodiac_sign = get_zodiac_sign(date.month, date.day).lower()

        return self.zodiac_sign
        
    
    def get_horoscope(self, url, zodiac_sign = None):

        if zodiac_sign == None:
            url = url + self.zodiac_sign + '/'
        else:
            url = url + zodiac_sign + '/'

        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')

        return soup.find(itemprop='articleBody')


        