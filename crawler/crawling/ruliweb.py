import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()

from bs4 import BeautifulSoup
import requests
from crawler.models import Ruliweb
from crawler.db.post.crawling_data import save_data


def ruliweb_list():
    web_url = requests.get('https://bbs.ruliweb.com/market/board/1020')
    result_list = []
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tbody > tr.table_body.blocktarget')
        for title in titles[4:32]:
            category = title.select_one('td.divsn.text_over > a[tabindex="-1"]')
            name = title.select_one('td.subject > div > a.deco')
            date = title.select_one('td.time')
            url = title.select_one('td.subject > div > a.deco').get('href')
            number = title.select_one('td.id')
            result_dict = \
                {
                    'number': number.text.strip(),
                    'category': category.text.strip(),
                    'name': name.text.strip(),
                    'date': date.text.strip(),
                    'url': url
                }
            result_list.append(result_dict)

        result_list = sorted(result_list, key=lambda x: x['number'])

    return result_list


def save_ruliweb_list(data):
    ruliweb_obj = Ruliweb(
        number=data['number'],
        category=data['category'],
        name=data['name'],
        date=data['date'],
        url=data['url']
    )
    save_data(ruliweb_obj)
