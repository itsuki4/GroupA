from django.urls import path
from . import views

app_name= 'itsuki'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('list/', views.DiaryListView.as_view(), name="diary_list"),
    path('detail/<int:pk>/',views.DiaryDetailView.as_view(), name="diary_detail"),
    path('create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('update/<int:pk>/',views.DiaryUpdateView.as_view(),name="diary_update"),
     path('delete/<int:pk>/',views.DiaryDeleteView.as_view(),name="diary_delete"),
]