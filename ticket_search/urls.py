from django.contrib import admin
from django.urls import path, include
from ticket_search import views

app_name = 'ticket_search'
urlpatterns = [
    path('', views.index, name='index'),
]
