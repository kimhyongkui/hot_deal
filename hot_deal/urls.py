from django.urls import path
from crawler import views

urlpatterns = [
    path('fmkorea/', views.fmkorea_list, name='fmkorea_list'),
    path('fmkorea/<int:pk>/', views.fmkorea_detail, name='fmkorea_detail'),
]
