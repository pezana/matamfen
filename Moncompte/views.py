from ast import Return
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from yaml import serialize



from .forms import loginForm
from .serializers import *
from .models import *


# Create your views here.
# declaration de la variable globale a_nom
def connexion(request):   
    msg=''
    form=loginForm() 
    if len(request.POST)>0:
        form=loginForm(request.POST)
        if form.is_valid(): 
            moi=inscription.objects.get(inslogin=form.cleaned_data['pseudo'] ,insmdp=form.cleaned_data['mdp'])
            response =redirect('bienvenue')
            response.set_cookie( 'moi_id',moi.id)                             
            return response
        else:
            msg='Vos information ne sont pas correctes'
            return render(request,'connexion.html',{'form':form,'msg':msg}) 
    else:
        msg=''
        form=loginForm()
        return render(request,'connexion.html',{'form':form,'msg':msg})    

def deconnexion(request):   
        form=loginForm()
        responce= render(request,'connexion.html',{'form':form})
        responce.set_cookie('moi_id','')
        return responce    
    
    
def bienvenue(request): 
    logged_user=get_logger_user_id_from_request(request)
    if logged_user: 
        return render(request,'menu.html',{'logged_user':logged_user})  
    else:
        return redirect('connexion')  
    
def syllabus(request):  
    logged_user=get_logger_user_id_from_request(request)
    if logged_user: 
        return render(request,'syllabus.html',{'logged_user':logged_user})  
    else:
        return redirect('connexion')     

def mesnotes(request):
    logged_user=get_logger_user_id_from_request(request)
    if logged_user: 
        return render(request,'mesnotes.html',{'logged_user':logged_user})  
    else:
        return redirect('connexion') 
     

def get_logger_user_id_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id =request.session['logged_user_id']  
        if len(inscription.objects.filter(pk=logged_user_id))==1:
            return inscription.objects.get(pk=logged_user_id) 
        else:
            return None
    else:
        return None
  

@api_view(['GET', 'POST', 'DELETE'])
def formationapi(request):
    if request.method=='GET':
        training=formation.objects.all()
        serializer=formationserialiser(training,many=True) 
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        training=JSONParser().parse(request)
        serializer=formationserialiser(data=training,many=True)
        if serializer.is_valid():
            serializer.save()
            reaffectationformation()            
            return JsonResponse('enregistrement avec succès',safe=False)
        return JsonResponse('echec d enregistrement123',safe=False)

def reaffectationformation(request):
    for inscrit in inscription:
        if inscrit.formation!='':
            maformation=get_object_or_404(formation,idf=inscrit.idf)
            inscrit.formation=maformation
            inscrit.save()     
      
@api_view(['GET', 'POST', 'DELETE'])     
def etudiantapi(request):
    if request.method=='GET':
        student=etudiant.objects.all()
        serializer=etudiantserializer(student,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        student=JSONParser().parse(request)
        serializer=etudiantserializer(data=student,many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('enregistrement avec succes',safe=False)
        return JsonResponse('echec',safe=False)
        
        
        

            
                   
        
    
   
                