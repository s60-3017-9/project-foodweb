from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'food'
urlpatterns = [

    # path('', views.search, name='search'),

    path('', views.show, name='show'),

    path('<int:restaurant_id>/', views.detail, name='detail'),
]