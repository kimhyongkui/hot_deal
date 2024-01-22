import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()


def save_data_fmkorea(fmkorea_obj):
    fmkorea_obj.save()


def save_data_ppomppu(ppomppu_obj):
    ppomppu_obj.save()


def save_data_ruliweb(ruliweb_obj):
    ruliweb_obj.save()
