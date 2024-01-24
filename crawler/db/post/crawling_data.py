import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.development")

import django

django.setup()


def save_data(obj):
    obj.save()
