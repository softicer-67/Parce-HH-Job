import json
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup as bs


class Engine(ABC):

    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def get_request(self, options=None, pages=0):
        self.options = options
        self.pages = pages
        super().get_request()
        hh_data = {}
        for page in range(self.pages):
            with open('hh_data.json', 'w', encoding='utf-8') as f:
                json.dump(hh_data, f, indent=4, ensure_ascii=False)
            try:
                current_data = json.loads(
                    requests.get(f"https://api.hh.ru/vacancies?text={self.options}&per_page={page}").text)
                print(f'[+] Парсим hh.ru Please wait ... {page + 1}')

                for i in range(page):
                    for item in current_data['items']:
                        hh_data[item['id']] = {
                            'title': item['name'].lower(),
                            'url': item['alternate_url'],
                            'salary': item['salary'],
                            'description': str(item['snippet']['requirement']).replace('<highlighttext>', '').replace(
                                '</highlighttext>', ''),
                            'date': item['published_at']
                        }
                with open('hh_data.json', 'w', encoding='utf-8') as f:
                    json.dump(hh_data, f, indent=4, ensure_ascii=False)
            except KeyError:
                print(f'[+] Error')
                break
        return hh_data

    @staticmethod
    def load_file():
        res = []
        with open('hh_data.json', 'r', encoding='utf-8') as f:
            top_10 = json.load(f)
        for k, v in top_10.items():
            try:
                date = v['date'][:10]
                date = f'{date[-2:]}-{date[5:7]}-{date[:4]}'
                res.append(
                    f"{date} {v['title']} от {v['salary']['from']} до "
                    f"{v['salary']['to']} руб. {v['url']} {v['description'][:50]}...")
            except TypeError:
                continue
        return '\n'.join(res)


class Superjob(Engine):
    def get_request(self):
        super().get_request()

    @staticmethod
    def load_file_2(options, pages):
        super_data = {}
        for page in range(pages):
            http = 'https://www.superjob.ru'
            url = f'https://russia.superjob.ru/vacancy/search/?keywords={options}&page={page}'
            print(f'[+] Парсим superjob.ru Please wait ... {page + 1}')
            response = requests.get(url)
            soup = bs(response.text, 'lxml')
            title = soup.find_all('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')
            salary = soup.find_all('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')
            desc = soup.find_all('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky')
            for i in range(pages):
                try:
                    super_data[i] = {
                            'title': title[i].text,
                            'salary': salary[i].text.replace('\xa0', ' '),
                            'url': http + title[i].a['href'],
                            'desc': desc[i].text
                        }
                    with open('super_data.json', 'w', encoding='utf-8') as f:
                        json.dump(super_data, f, indent=4, ensure_ascii=False)
                except IndexError:
                    continue

        return super_data

