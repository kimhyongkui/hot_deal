from django.urls import path
from .views import post_list_view

urlpatterns = [
    path('post-list/', post_list_view, name='post_list'),
]
