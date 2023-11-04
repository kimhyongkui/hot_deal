import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings")

import django

django.setup()

from django.shortcuts import render
from crawler.models import Fmkorea


def fmkorea_list(request):
    tasks = Fmkorea.objects.all()
    return render(request, 'fmkorea_list.html', {'tasks': tasks})


def fmkorea_detail(request, pk):
    task = Fmkorea.objects.get(id=pk)
    return render(request, 'fmkorea_detail.html', {'task': task})
