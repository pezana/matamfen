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
        

class anneeserialiser(serializers.ModelSerializer):
    class Meta():
        model=anneeacademique
        fields='__all__'  
      
class profmatiereserialiser(serializers.ModelSerializer):
    class Meta():
        model=profmatiere
        fields='__all__'  
                        
class noteserialiser(serializers.ModelSerializer):
    class Meta():
        model=notes
        fields='__all__'  
                                       