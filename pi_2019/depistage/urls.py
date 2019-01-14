from django.urls import path 
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('', views.connexion, name='connexion'),
    path('accueil/', views.accueil, name='accueil'),


]