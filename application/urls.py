from django.urls import path
from . import views

app_name = "application"

urlpatterns = [
    path('vetements/', views.viewVetements, name='viewVetements'),
    path("", views.list_view, name="index"),
    path("", views.home, name="home"),
]