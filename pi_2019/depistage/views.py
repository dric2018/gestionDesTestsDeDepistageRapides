# -*- coding: utf-8 -*-
from depistage.forms import LoginForm
from django.shortcuts import render, redirect

def accueil(request):
    #ajouter ici les parametres a convertir avant la confection de la page html
    
    return render(request, 'depistage/accueil.html')


def connexion(request):
    #ajouter ici les parametres a convertir avant la confection de la page html
    
    #teste si le formulaire est envoye
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('accueil/')
        else: 
            return render(request, 'depistage/connexion.html', {'form': form})
    
    else:
        form = LoginForm()
        return render(request, 'depistage/connexion.html', {'form': form})




