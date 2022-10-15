from django.urls import path
from . import views

urlpatterns = [
    path("companies/", views.get_companies),
    path("company/<str:id>/", views.get_single_company),
    path("advocates/", views.get_advocates), 
    path("advocate/<str:id>/", views.get_single_advocate)
]