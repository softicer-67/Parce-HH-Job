import json

import requests
from abc import ABC, abstractmethod


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
    def __init__(self, request_name):
        self.name = request_name
        self.url = 'http://russia.superjob.ru/vacancy/search/'

    def get_request(self, page_num):
        par = {'keywords': self.name, 'page': page_num}
        return requests.get(self.url, params=par)


# class Vacancy:
#     def __init__(self, data, hh=False):
#         self.data = data
#         self.hh = hh
#         self.name = self.set_name()
#         self.salary = self.set_salary()
#         self.description = self.set_description()
#         self.url = self.set_url()
#
#     def __repr__(self):
#         return f'{self.name}|{self.description}|{self.url}|{self.salary}'
#
#     def set_name(self):
#         if self.hh:
#             return self.data['name']
#         name = self.data.contents[3].text
#         return name.replace(self.data.contents[3].contents[0].contents[1].text, '')
#
#     def set_salary(self):
#         if self.hh:
#             try:
#                 salary = self.data['salary']['from']
#                 return salary
#             except:
#                 return 0
#         pattern = re.compile(r"\d+")
#         salary = self.data.contents[3].contents[0].contents[1].text
#         salary = ''.join(re.findall(pattern, salary))
#         if salary:
#             return int(salary)
#         return 0
#
#     def set_description(self):
#         if self.hh:
#             if self.data['snippet']['requirement'] and self.data['snippet']['responsibility']:
#                 return self.data['snippet']['requirement'] + self.data['snippet']['responsibility']
#             else:
#                 try:
#                     return self.data['snippet']['requirement']
#                 except:
#                     return self.data['snippet']['responsibility']
#         desc = self.data.contents[5].text
#         return desc
#
#     def set_url(self):
#         if self.hh:
#             return self.data['alternate_url']
#         link = self.data.contents[3].findAll('a')[0].attrs['href']
#         return 'https://russia.superjob.ru' + link

