from django.shortcuts import render
from app.utils.post_list import post_list
from app.models import ListData
from app.crawling.ppomppu import ppomppu_list


def post_list_view(request):
    if request.method == 'POST':
        post_list()
    return render(request, 'post_list.html')


def post_data():
    ppomppu_list_data = ppomppu_list()
    for data in ppomppu_list_data:
        result = ListData(
            name=data['name'],
            category=data['category']
        )
        result.save()
