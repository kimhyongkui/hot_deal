import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()

from bs4 import BeautifulSoup
import requests
from crawler.models import Ruliweb
from crawler.notification.discord_noti import send_discord_notification
from crawler.db.post.crawling_data import save_data_ruliweb

def ruliweb():
    web_url = requests.get('https://bbs.ruliweb.com/market/board/1020')
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
            print(category.text.strip())
            print(name.text.strip())
            print(date.text.strip())
            print(url)
            print(number.text.strip())
            print('------------------------------')


# def ruliweb_list():
#     web_url = requests.get('https://bbs.ruliweb.com/market/board/1020')
#     if web_url.status_code == 200:
#         html = web_url.text
#         soup = BeautifulSoup(html, 'html.parser')
#         titles = soup.select('tbody > tr.table_body.blocktarget')
#         result_list = []
#         for title in titles[4:32]:
#             category = title.select_one('td.divsn.text_over > a[tabindex="-1"]')
#             name = title.select_one('td.subject > div > a.deco')
#             date = title.select_one('td.time')
#             url = title.select_one('td.subject > div > a.deco').get('href')
#             number = title.select_one('td.id')
#             result_dict = \
#                 {
#                     'number': number.text.strip(),
#                     'category': category.text.strip(),
#                     'name': name.text.strip(),
#                     'date': date.text.strip(),
#                     'url': url
#                 }
#             result_list.append(result_dict)
#
#         result_list = sorted(result_list, key=lambda x: x['number'])
#
#         return result_list

def ruliweb_list():
    web_url = requests.get('https://bbs.ruliweb.com/market/board/1020')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tbody > tr.table_body.blocktarget')
        result_list = []
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


def count_list(ruliweb_list):
    data_list = ruliweb_list()
    new_list = []
    for data in data_list:
        check_data = Ruliweb.objects.filter(url=data['url']).first()
        if not check_data:
            new_list.append(data)
    return new_list
