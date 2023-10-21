from myapps.models import Fmkorea, Ppomppu, Ruliweb


def get_fmkorea_data():
    result = Fmkorea.objects.all()
    return result

def get_ppomppu_data():
    result = Ppomppu.objects.all()
    return result

def get_ruliweb_data():
    result = Ruliweb.objects.all()
    return result