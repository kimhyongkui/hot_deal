import os
import django
from hot_deal import settings
from app.crawling.ppomppu import ppomppu_list
from app.models import ListData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings.base")
django.setup()

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings['default']['USER']}:{settings['default']['PASSWORD']}@{settings['default']['HOST']}/{settings['default']['NAME']}"
# SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{os.getenv('USER')}:{os.getenv('USER_PWD')}@{os.getenv('DB_HOST')}/bus_api"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

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