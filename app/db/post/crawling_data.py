from app.models import Fmkorea, Ppomppu, Ruliweb  # 필요한 모델 클래스를 가져옵니다.
from app.crawling.fmkorea import fmkorea_list


def save_data_to_database():
    for data in fmkorea_list:
        fmkorea_obj = Fmkorea(
            name=data['name'],
            category=data['category'],
            price=data['price']
        )
        fmkorea_obj.save()  # 데이터베이스에 저장합니다.


