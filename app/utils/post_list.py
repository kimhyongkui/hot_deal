import os
from app.crawling.ppomppu import ppomppu_list
from app.models import ListData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{os.getenv('USER')}:{os.getenv('USER_PWD')}@{os.getenv('DB_HOST')}/bus_api"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def post_data():
    ppomppu_list_data = ppomppu_list()
    Session = sessionmaker(bind=engine)
    session = Session()

    for data in ppomppu_list_data:
        result = ListData(
            name=data['name'],
            category=data['category']
        )
        session.add(result)
    session.commit()
    session.close()
