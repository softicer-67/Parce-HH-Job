from bs4 import BeautifulSoup
from classes import *


def get_hh_vacs(req_text: str, how_many: int) -> None:
    vacancies: dict = {}
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
        name = 'hh_data.json'
        data = Vacancy(name, vacancies)
        data.write_file()


def get_sj_vacs(req_text: str, pages) -> None:
    vacancies = {}
    sj = Superjob(req_text, pages)
    res = sj.get_request(0)
    soup = BeautifulSoup(res.text, 'lxml')
    date = soup.find_all('div', class_='_8zbxf _3nFt9 _3bJZe')
    title = soup.find_all('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')
    salary = soup.find_all('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')
    desc = soup.find_all('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky')
    try:
        for i in range(2, pages):
            id_ = title[i].a['href'][-13:-5:]
            vacancies[id_] = {
                'date': date[i].text,
                'title': title[i].text,
                'salary': salary[i].text.replace('\xa0', ' '),
                'url': 'http://russia.superjob.ru' + title[i].a['href'],
                'desc': desc[i].text
            }
    except IndexError:
        pass
    name = 'sj_data.json'
    data = Vacancy(name, vacancies)
    data.write_file()


def output_hh():
    vac_list = []
    with open('hh_data.json', 'r', encoding='utf-8') as file:
        all_list = json.load(file)
    for k, v in all_list.items():
        try:
            vac_list.append(
                f"{v['date'][:10]} {v['title']} от {v['salary']['from']} до "
                f"{v['salary']['to']} руб. {v['url']} {v['description'][:50]}...")
        except TypeError:
            continue
    return vac_list


def output_sj() -> list:
    vac_list = []
    with open('sj_data.json', 'r', encoding='utf-8') as f:
        all_list = json.load(f)
    for k, v in all_list.items():
        try:
            vac_list.append(
                f"{v['date']} {v['title']} {v['salary']} {v['url']} {v['desc'][:50]}...")
        except TypeError:
            continue
    return vac_list
