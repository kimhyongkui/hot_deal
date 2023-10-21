import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings")

import django

django.setup()

from crawler.models import Fmkorea, Ppomppu, Ruliweb
from crawler.crawling.fmkorea import fmkorea_list
from crawler.crawling.ppomppu import ppomppu_list
from crawler.crawling.ruliweb import ruliweb_list


def save_data_fmkorea():
    data_list = fmkorea_list()
    for data in data_list:
        fmkorea_obj = Fmkorea(
            name=data['name'],
            shop=data['shop'],
            price=data['price'],
            deliver=data['deliver']
        )
        fmkorea_obj.save()


def save_data_ppomppu():
    data_list = ppomppu_list()
    for data in data_list:
        ppomppu_obj = Ppomppu(
            name=data['name'],
            category=data['category']
        )
        ppomppu_obj.save()


def save_data_ruliweb():
    data_list = ruliweb_list()
    for data in data_list:
        ruliweb_obj = Ruliweb(
            name=data['name']
        )
        ruliweb_obj.save()

save_data_ruliweb()