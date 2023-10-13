from app.models import Fmkorea, Ppomppu, Ruliweb
from app.crawling.fmkorea import fmkorea_list
from app.crawling.ppomppu import ppomppu_list
from app.crawling.ruliweb import ruliweb_list
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hot_deal.settings')
django.setup()


def save_data_fmkorea():
    for data in fmkorea_list:
        fmkorea_obj = Fmkorea(
            name=data['name'],
            shop=data['shop'],
            price=data['price'],
            deliver=data['deliver']
        )
        fmkorea_obj.save()


def save_data_ppomppu():
    for data in ppomppu_list:
        ppomppu_obj = Ppomppu(
            name=data['name'],
            category=data['category']
        )
        ppomppu_obj.save()


def save_data_ruliweb():
    for data in ruliweb_list:
        ruliweb_obj = Ruliweb(
            name=data['name']
        )
        ruliweb_obj.save()
