from . import views
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [    
    path('',views.connexion,name='connexion'),
    path('connexion',views.deconnexion,name='deconnexion'),
    path('bienvenue',views.bienvenue,name='bienvenue'),
    path('syllabus',views.syllabus,name='syllabus'),
    path('mesnotes',views.mesnotes,name='mesnotes'),
    path('formation_api/',csrf_exempt(views.formationapi)), 
    path('etudiant_api/',csrf_exempt(views.etudiantapi)),  
]
