import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()

from crawler.models import Fmkorea
from crawler.crawling.fmkorea import fmkorea_list
from crawler.notification.discord_noti import send_discord_notification
from django.db import IntegrityError


def save_data_fmkorea():
    data_list = fmkorea_list()
    new_post_count = 0
    for data in data_list:
        try:
            check_data = Fmkorea.objects.filter(url=data['url']).first()
            if not check_data:
                fmkorea_obj = Fmkorea(
                    name=data['name'],
                    shop=data['shop'],
                    price=data['price'],
                    deliver=data['deliver'],
                    date=data['date'],
                    url=data['url']
                )
                fmkorea_obj.save()
                new_post_count += 1

        except IntegrityError as err:
            pass

    if new_post_count >= 0:
        print(f"{new_post_count}개 업데이트")
        message = f"fmkorea : {new_post_count}개 업데이트"
        send_discord_notification(message)


def save_data_ppomppu(ppomppu_obj):
    ppomppu_obj.save()


def save_data_ruliweb(ruliweb_obj):
    ruliweb_obj.save()
