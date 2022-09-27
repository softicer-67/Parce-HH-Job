import time
import requests
import json


def get_data(option, page):

    url = f'https://api.hh.ru/vacancies?text={option}&only_with_salary=true&specialization=1.221&per_page={page}&area=1'

    filter_data = {}
    for page in range(page):
        try:
            current_data = json.loads(
                requests.get(
                    url + f"&page={page}"
                ).text
            )

            for item in current_data['items']:
                filter_data.update({
                    item['id']: {
                        'title': item['name'].lower(),
                        'url': item['alternate_url'],
                        'salary': item['salary'],
                        'description': str(
                            item['snippet']['requirement']).replace('<highlighttext>', '').replace('</highlighttext>', '')

                    }})
            print(f'[+] Please wait ... str. {page}')
        except KeyError:
            continue
        time.sleep(0.3)

    with open('all_data.json', 'w', encoding='utf-8') as f:
        json.dump(filter_data, f, indent=4, ensure_ascii=False)

