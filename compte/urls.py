from django.urls import path
from . import views

app_name = "compte"
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('deleteProfile/<str:username>/', views.deleteProfile, name='deleteProfile'),
    path('deleteProfileClassique/<str:username>/', views.deleteProfileClassique, name='deleteProfileClassique'),
    path('user_list/', views.user_list, name='user_list'),
]