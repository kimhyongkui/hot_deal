from django.urls import path
from crawler import views

urlpatterns = [
    path('fmkorea/', views.fmkorea_list, name='fmkorea_list'),
    path('fmkorea/<int:pk>/', views.fmkorea_detail, name='fmkorea_detail'),
    path('ppomppu/', views.ppomppu_list, name='ppomppu_list'),
    path('ppomppu/<int:pk>/', views.ppomppu_detail, name='ppomppu_detail'),
    path('ruliweb/', views.ruliweb_list, name='ruliweb_list'),
    path('ruliweb/<int:pk>/', views.ruliweb_detail, name='ruliweb_detail')
]
