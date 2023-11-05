import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hot_deal.settings")

import django

django.setup()

from django.shortcuts import render
from crawler.models import Fmkorea, Ppomppu, Ruliweb


def fmkorea_list(request):
    tasks = Fmkorea.objects.all()
    return render(request, 'fmkorea_list.html', {'tasks': tasks})


def fmkorea_detail(request, pk):
    task = Fmkorea.objects.get(id=pk)
    return render(request, 'fmkorea_detail.html', {'task': task})


def ppomppu_list(request):
    tasks = Ppomppu.objects.all()
    return render(request, 'ppomppu_list.html', {'tasks': tasks})


def ppomppu_detail(request, pk):
    task = Ppomppu.objects.get(id=pk)
    return render(request, 'ppomppu_detail.html', {'task': task})


def ruliweb_list(request):
    tasks = Ruliweb.objects.all()
    return render(request, 'ruliweb_list.html', {'tasks': tasks})


def ruliweb_detail(request, pk):
    task = Ruliweb.objects.get(id=pk)
    return render(request, 'ruliweb_detail.html', {'task': task})
