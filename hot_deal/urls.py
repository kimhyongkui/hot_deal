from django.urls import path
from app.utils.post_list import post_data


urlpatterns = [
    path('post-list/', post_data, name='post_data'),
]
