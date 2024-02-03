import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()

from crawler.notification.discord_noti import send_discord_notification
from crawler.models import Fmkorea, Ppomppu, Ruliweb
from crawler.crawling.fmkorea import fmkorea_list, save_fmkorea_list
from crawler.crawling.ppomppu import ppomppu_list, save_ppomppu_list
from crawler.crawling.ruliweb import ruliweb_list, save_ruliweb_list


def send_notify(site_name, new_post_count, message_list):
    if new_post_count >= 0:
        message_list.append(f"{site_name} : {new_post_count}개 업데이트")
        send_discord_notification(message_list)


def count_list(site_name):
    try:
        data_list = globals()[f"{site_name}_list"]()

        if data_list is None or not data_list:
            raise ValueError(f"{site_name} 데이터 없음")

        new_post_count = 0
        message_list = []

        for data in data_list:
            check_data = globals()[site_name.capitalize()].objects.filter(url=data['url']).first()
            if not check_data:
                globals()[f"save_{site_name}_list"](data)
                message_list.append(f"{data['name']}")
                new_post_count += 1

        send_notify(site_name, new_post_count, message_list)

    except ValueError as err:
        print(err)

    except Exception as err:
        print(err)
