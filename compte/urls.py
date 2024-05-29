from django.urls import path
from . import views

app_name = "compte"
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('',views.index,name='index'),
    path('<int:pk>/profile/', views.profile, name='profile'),

]