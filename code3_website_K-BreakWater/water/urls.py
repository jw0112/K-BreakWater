from django.contrib import admin
from django.urls import path
from . import views

# ''자기 자신이면 views안에 water 함수 연결
# <str:city>가 주소로 들어오면 views안에 city_detail로 연결
urlpatterns = [
    path('', views.water),
    path('<str:city>/', views.city_detail)
]

