import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()

from crawler.models import Fmkorea, Ppomppu, Ruliweb


def get_fmkorea_data():
    result = Fmkorea.objects.all()
    return result


def get_ppomppu_data():
    result = Ppomppu.objects.all()
    return result


def get_ruliweb_data():
    result = Ruliweb.objects.all()
    return result
