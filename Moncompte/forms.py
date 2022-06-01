from logging import PlaceHolder
from django import forms

from django.forms import formset_factory
from django.shortcuts import get_object_or_404
from .models import *

class loginForm(forms.Form):
    pseudo=forms.CharField()
    mdp=forms.CharField(label='Mot de passe', widget=forms.PasswordInput())
    
    def clean(self):
        clean_data=super(loginForm,self).clean()
        pseudo=clean_data.get('pseudo')
        mdp=clean_data.get('mdp')
        if pseudo and mdp:
           inscript=inscription.objects.filter(inslogin=pseudo,insmdp=mdp)
           if len(inscript)!=1:               
               raise forms.ValidationError('vos informations ne sont pas correctes')
        else:
            raise forms.ValidationError('Entrer vos accès')  
        
        return clean_data      
           