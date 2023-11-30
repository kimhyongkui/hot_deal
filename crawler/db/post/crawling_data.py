import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()

from crawler.models import Fmkorea, Ppomppu, Ruliweb
from crawler.crawling.fmkorea import fmkorea_list
from crawler.crawling.ppomppu import ppomppu_list
from crawler.crawling.ruliweb import ruliweb_list


def save_data_fmkorea():
    data_list = fmkorea_list()
    new_posts_count = 0
    for data in data_list:
        check_data = Fmkorea.objects.filter(name=data['name']).first()
        if check_data:
            continue

        fmkorea_obj = Fmkorea(
            name=data['name'],
            shop=data['shop'],
            price=data['price'],
            deliver=data['deliver'],
            date=data['date'],
            url=data['url']
        )
        fmkorea_obj.save()
        new_posts_count += 1
    if new_posts_count >= 0:
        print(f"{new_posts_count}개 업데이트")


def save_data_ppomppu():
    data_list = ppomppu_list()
    new_posts_count = 0
    for data in data_list:
        check_data = Ppomppu.objects.filter(number=data['number']).first()
        if check_data:
            continue

        ppomppu_obj = Ppomppu(
            number=data['number'],
            category=data['category'],
            name=data['name'],
            date=data['date'],
            url=data['url']
        )
        ppomppu_obj.save()
        new_posts_count += 1
    if new_posts_count >= 0:
        print(f"{new_posts_count}개 업데이트")


def save_data_ruliweb():
    data_list = ruliweb_list()
    new_posts_count = 0
    for data in data_list:
        check_data = Ruliweb.objects.filter(number=data['number']).first()
        if check_data:
            continue
        ruliweb_obj = Ruliweb(
            number=data['number'],
            category=data['category'],
            name=data['name'],
            date=data['date'],
            url=data['url']
        )
        ruliweb_obj.save()
        new_posts_count += 1
    if new_posts_count >= 0:
        print(f"{new_posts_count}개 업데이트")
