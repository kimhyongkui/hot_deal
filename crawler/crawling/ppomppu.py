import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()

from bs4 import BeautifulSoup
import requests
from crawler.models import Ppomppu
from crawler.notification.discord_noti import send_discord_notification
from crawler.db.post.crawling_data import save_data


def ppomppu_list():
    web_url = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    if web_url.status_code == 200:
        html = web_url.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('tr td:nth-child(2) > div')
        dates = soup.select('td:nth-child(4) > nobr')
        numbers = soup.select('td.eng.list_vspace[colspan="2"]')
        result_list = []
        for title, date, number in zip(titles[3:42:2], dates[1:22:1], numbers[6::4]):
            category = title.select_one('span[style="color:#999;font-size:11px;"]')
            name = title.select_one('a > font.list_title')
            date_text = date.text.strip()
            url = title.select_one('a').get('href')
            number_text = number.text.strip()
            if name is not None:
                result_dict = \
                    {
                        'number': number_text,
                        'category': category.text.strip(),
                        'name': name.text.strip(),
                        'date': date_text,
                        'url': f"https://www.ppomppu.co.kr/zboard/{url}"
                    }
                result_list.append(result_dict)

        result_list = sorted(result_list, key=lambda x: x['number'])

        return result_list


def count_ppomppu_list():
    data_list = ppomppu_list()
    new_post_count = 0
    message_list = []
    for data in data_list:
        check_data = Ppomppu.objects.filter(url=data['url']).first()
        if not check_data:
            ppomppu_obj = Ppomppu(
                number=data['number'],
                category=data['category'],
                name=data['name'],
                date=data['date'],
                url=data['url']
            )
            save_data(ppomppu_obj)
            message_list.append(f"{data['name']}")
            new_post_count += 1
    if new_post_count >= 0:
        message_list.append(f"ruliweb : {new_post_count}개 업데이트")
        send_discord_notification(message_list)
