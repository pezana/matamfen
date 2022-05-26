from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *

class formationserialiser(serializers.ModelSerializer):
    class Meta():
        model=formation
        fields='__all__'
        
class etudiantserializer(serializers.ModelSerializer):
    class Meta():
        model=etudiant
        fields='__all__'
        
class inscriptionserializer(serializers.ModelSerializer):
    class Meta():
        model=inscription
        fields='__all__'        
                