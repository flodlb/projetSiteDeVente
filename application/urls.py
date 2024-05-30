from django.urls import path
from . import views

app_name = "application"

urlpatterns = [
    path("Zoom/<int:pk>/", views.viewZoom, name="viewZoom"),
    path('vetements/', views.viewVetements, name='viewVetements'),
    path('panier/', views.viewPanier, name='viewPanier'),
    path("", views.list_view, name="index"),
    path("", views.home, name="home"),
]