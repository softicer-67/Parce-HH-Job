import json
import requests
from abc import ABC, abstractmethod
from utils import *


class Engine(ABC):
    @abstractmethod
    def get_request(self, page):
        pass
      

class HH(Engine):
    def __init__(self, request_name, quantity):
        self.name = request_name
        self.iter = int(quantity / 100)
        self.url = 'http://api.hh.ru/vacancies'
        
    def get_request(self, page_num):
        par = {'text': self.name, 'page': page_num, 'per_page': 100, 'area': 113}
        return requests.get(self.url, params=par)


class Superjob(Engine):
    def __init__(self, request_name, quantity):
        self.name = request_name
        self.iter = int(quantity / 100)
        self.url = 'http://russia.superjob.ru/vacancy/search/'

    def get_request(self, page_num):
        par = {'keywords': self.name, 'page': page_num}
        return requests.get(self.url, params=par)


class Vacancy:
    def __init__(self, name, vacancies):
        self.name = name
        self.vacancies = vacancies

    def write_file(self):
        with open(self.name, 'w', encoding='utf-8') as f:
            json.dump(self.vacancies, f, indent=4, ensure_ascii=False)
