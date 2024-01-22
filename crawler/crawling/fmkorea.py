import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()

from bs4 import BeautifulSoup
import requests
from crawler.models import Fmkorea
from crawler.notification.discord_noti import send_discord_notification
from crawler.db.post.crawling_data import save_data_fmkorea


def fmkorea_list():
    web_url = requests.get('https://www.fmkorea.com/hotdeal')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('div > div > div > ul > li.li')
        result_list = []
        for title in titles:
            name = title.select_one('div > h3 > a')
            shop = title.select_one('div > div > span:nth-child(1)')
            price = title.select_one('div > div > span:nth-child(2)')
            deliver = title.select_one('div > div > span:nth-child(3)')
            date = title.select_one('div > div > span.regdate')
            url = name.get('href')
            result_dict = \
                {
                    'name': name.text.strip(),
                    'shop': shop.text.strip(),
                    'price': price.text.strip(),
                    'deliver': deliver.text.strip(),
                    'date': date.text.strip(),
                    'url': f"https://www.fmkorea.com/{url}"
                }
            result_list.append(result_dict)

        result_list = sorted(result_list, key=lambda x: x['date'])

        return result_list


def count_list():
    data_list = fmkorea_list()
    new_post_count = 0
    message_list = []
    for data in data_list:
        check_data = Fmkorea.objects.filter(url=data['url']).first()
        if not check_data:
            fmkorea_obj = Fmkorea(
                name=data['number'],
                shop=data['shop'],
                price=data['price'],
                deliver=data['deliver'],
                date=data['date'],
                url=data['url']
            )
            save_data_fmkorea(fmkorea_obj)
            message_list.append(f"{data['name']}")
            new_post_count += 1
    if new_post_count >= 0:
        message_list.append(f"ruliweb : {new_post_count}개 업데이트")
        send_discord_notification(message_list)
