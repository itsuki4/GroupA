from django.contrib import admin
from django.urls import path

from . import views

app_name = 'itsuki'
urlpatterns = [
    path('itsuki',views.IndexView.as_view(), name="index"),
    path('list/',views.DiaryListView.as_view(),name="list"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('detail/<int:pk>',views.DiaryDetailView.as_view(),name="detail"),
    path('create/',views.DiaryCreateView.as_view(),name="create"),
    path('update/<int:pk>/',views.DiaryUpdateView.as_view(),name="update"),
    path('delete/<int:pk>/',views.DiaryDeleteView.as_view(),name="delete"),
]
