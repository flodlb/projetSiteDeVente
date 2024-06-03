from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
    path("<int:pk>/update/", views.update_view, name='update'),
    path("<int:pk>/delete/", views.delete_view, name="delete"),
    path('historique', views.viewHistorique, name='viewHistorique'),
    path('ValidePanier', views.ValidePanier, name='ValidePanier'),
    path('addtopanier/<int:pk>/', views.addToPanier, name='addToPanier'),
    path("Zoom/<int:pk>/", views.viewZoom, name="viewZoom"),
    path('vetements/', views.viewVetements, name='viewVetements'),
    path('panier/', views.viewPanier, name='viewPanier'),
    path("", views.list_view, name="index"),
    path("", views.home, name="home"),
]