import json
from abc import ABC, abstractmethod
import requests


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, options=None, pages=0):
        self.options = options
        self.pages = pages

    @staticmethod
    def load_file():
        res = []
        with open('all_data.json', 'r', encoding='utf-8') as f:
            top_10 = json.load(f)
        for k, v in top_10.items():
            try:
                date = v['date'][:10]
                date = f'{date[-2:]}-{date[5:7]}-{date[:4]}'
                res.append(
                    f"{date} {v['title']} от {v['salary']['from']} до {v['salary']['to']} руб. {v['url']} {v['description'][:50]}...")
            except TypeError:
                continue
        return '\n'.join(res)

    def get_request(self):
        filter_data = {}
        for page in range(self.pages):
            try:
                current_data = json.loads(requests.get(f"https://api.hh.ru/vacancies?text={self.options}&per_page={page+1}").text)
                print(f'[+] Please wait ... str. {page + 1}')
                for i in range(page):
                    for item in current_data['items']:
                        filter_data[item['id']] = {
                            'title': item['name'].lower(),
                            'url': item['alternate_url'],
                            'salary': item['salary'],
                            'description': str(item['snippet']['requirement']).replace('<highlighttext>', '').replace('</highlighttext>', ''),
                            'date': item['published_at']
                        }
                with open('all_data.json', 'w', encoding='utf-8') as f:
                    json.dump(filter_data, f, indent=4, ensure_ascii=False)
            except KeyError:
                print(f'[+] Error')
                break
        with open('all_data.json', 'w', encoding='utf-8') as f:
            json.dump(filter_data, f, indent=4, ensure_ascii=False)
        return filter_data


class Superjob(Engine):
    def get_request(self):
        pass


