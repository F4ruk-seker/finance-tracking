from bs4 import BeautifulSoup
import requests


class ShareScraper:
    def __init__(self, *args, **kwargs):
        self.__result: list[dict] = [{}]
        self.target = 'https://borsa.doviz.com/hisseler'

    def get_content(self):
        if response := requests.get(self.target):
            return response.content

    def get_soup(self):
        if content := self.get_content():
            return BeautifulSoup(content)

