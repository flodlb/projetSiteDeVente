from django.conf.urls.static import static
from django.urls import path

from projetSiteDeVente import settings
from . import views

app_name = 'application'

urlpatterns = [

    path("ajouter/", views.createProduct, name='createProduct'),
    path("<int:pk>/modifier/", views.updateProduct, name='modifierProduct'),
    path("<int:pk>/delete/", views.deleteProduct, name="deleteProduct"),
    path('historique', views.viewHistorique, name='viewHistorique'),
    path('ValidePanier', views.ValidePanier, name='ValidePanier'),
    path('addtopanier/<int:pk>/', views.addToPanier, name='addToPanier'),
    path("Zoom/<int:pk>/", views.viewZoom, name="viewZoom"),
    path('vetements/', views.viewVetements, name='viewVetements'),
    path('panier/', views.viewPanier, name='viewPanier'),
    path("index/", views.list_view, name="index"),
    path("", views.home, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)