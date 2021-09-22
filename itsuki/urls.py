from django.contrib import admin
from django.urls import path

from . import views

app_name = 'itsuki'
urlpatterns = [
    path('itsuki',views.Indexview.as_view(), name="index"),
]
