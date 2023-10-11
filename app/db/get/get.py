from app.models import Fmkorea


def get_fmkorea_data():
    result = Fmkorea.objects.all()
