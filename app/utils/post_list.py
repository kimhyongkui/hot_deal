import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings")

import django

django.setup()

from app.crawling.ppomppu import ppomppu_list
from app.models import ListData
from sqlalchemy.orm import sessionmaker
from app.utils.connection import engine

Session = sessionmaker(bind=engine)
session = Session()


def post_data():
    ppomppu_list_data = ppomppu_list()

    for data in ppomppu_list_data:
        result = ListData(
            name=data['name'],
            category=data['category']
        )
        session.add(result)
    session.commit()
    session.close()


print(post_data())
