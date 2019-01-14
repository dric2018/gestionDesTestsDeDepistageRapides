# -*- coding: utf-8 -*-
#gestion des fromulaires
from django import forms

class LoginForm(forms.Form):
    #les champs du formulaire
    email = forms.EmailField(label="Nom d'utilisateur")
    #vu que le champ PasswordField n'existe pas ...
    password = forms.CharField(label="Mot de passe",
                                            widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super (LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        #verification de la validite des champs
        if email and password:
            if password != "azertyuiop" or email != "manouancedric@gmail.com":
                raise forms.ValidationError("Adresse utilisateur ou mot de passe incorrect(e)")
        
        return cleaned_data