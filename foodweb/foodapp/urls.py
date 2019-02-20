from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'food'
urlpatterns = [

    # path('', views.search_restaurant, name='search'),

    path('', views.show_restaurant, name='show_res'),

    path('<int:restaurant_id>/', views.detail_restaurant, name='detail_res'),
]
