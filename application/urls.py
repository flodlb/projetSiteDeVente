from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
    path('vetements/', views.liste_vetements, name='liste_vetements'),
    path("", views.list_view, name="index"),
    path("", views.home, name="home"),
]