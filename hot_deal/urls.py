from django.urls import path
from app.views import post_list_view

urlpatterns = [
    path('post-list/', post_list_view, name='post_list'),
]
