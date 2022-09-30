import json

import requests
from bs4 import BeautifulSoup
from classes import HH, Superjob #, Vacancy


def write_file(data: list) -> None:
    with open('hh_data.json', 'w', encoding='utf-8') as f:
        for dt in data:
            json.dump(dt, f, indent=4, ensure_ascii=False)


def get_hh_vacs(req_text: str, how_many: int) -> None:
    vacancies = {}
    current_data = json.loads(
            requests.get(f"https://api.hh.ru/vacancies?text={req_text}&per_page={how_many}").text)
    for item in current_data['items']:
        vacancies[item['id']] = {
            'title': item['name'].lower(),
            'url': item['alternate_url'],
            'salary': item['salary'],
            'description': str(item['snippet']['requirement']).replace('<highlighttext>', '').replace(
                '</highlighttext>', ''),
            'date': item['published_at']
        }
        with open('hh_data.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)


def get_sj_vacs(req_text: str, pages) -> None:
    vacancies = {}
    sj = Superjob(req_text)
    res = sj.get_request(0)
    soup = BeautifulSoup(res.text, 'lxml')
    title = soup.find_all('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')
    salary = soup.find_all('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')
    desc = soup.find_all('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky')
    for i in range(2, pages):
        try:
            vacancies[i] = {
                'title': title[i].text,
                'salary': salary[i].text.replace('\xa0', ' '),
                'url': 'http://russia.superjob.ru' + title[i].a['href'],
                'desc': desc[i].text
            }
            with open('sj_data.json', 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, indent=4, ensure_ascii=False)
        except IndexError:
            continue


def output_hh():
    vac_list = []
    with open('hh_data.json', 'r', encoding='utf-8') as file:
        all_list = json.load(file)
    for k, v in all_list.items():
        try:
            date = v['date'][:10]
            date = f'{date[-2:]}-{date[5:7]}-{date[:4]}'
            vac_list.append(
                f"{date} {v['title']} от {v['salary']['from']} до "
                f"{v['salary']['to']} руб. {v['url']} {v['description'][:50]}...")
        except TypeError:
            continue
    return vac_list


def output_sj() -> list:
    vac_list_sj = []
    with open('sj_data.json', 'r', encoding='utf-8') as f:
        all_list = json.load(f)
    for k, v in all_list.items():
        try:
            # date = v['date'][:10]
            # date = f'{date[-2:]}-{date[5:7]}-{date[:4]}'
            vac_list_sj.append(
                f"{v['title']} от {v['salary']} руб {v['url']} {v['desc'][:50]}...")
        except TypeError:
            continue
    return vac_list_sj

