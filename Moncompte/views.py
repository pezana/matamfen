from ast import Return
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from yaml import serialize
from django.core.paginator import Paginator



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
            moi=inscription.objects.get(inslogin=form.cleaned_data['pseudo'],insmdp=form.cleaned_data['mdp'])
            request.session['logged_user_id']=moi.id
            return redirect('bienvenue')                         
        else:
            msg='Vos information ne sont pas correctes'
            form=loginForm()
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
        inscrit=inscription.objects.get(id=logged_user.id)
        syllabus=profmatiere.objects.filter(idfor=inscrit.idfor).order_by('semestre','codepm')
        ''' paginator=paginator(syllabus,5)
        page_number= request.GET.get('page') 
        query=paginator.get_page(page_number)  '''                    
        return render(request,'syllabus.html',{'logged_user':logged_user,'syl':syllabus})  
    else:
        return redirect('connexion')     

def mesnotes(request):
    logged_user=get_logger_user_id_from_request(request)
    if logged_user: 
        inscrit=inscription.objects.get(id=logged_user.id)
        note=notes.objects.filter(idins=inscrit.idins)#.order_by('profmatiere.semestre','profmatiere.matiere')
        return render(request,'mesnotes.html',{'logged_user':logged_user,'note':note})  
    else:
        return redirect('connexion')      

def get_logger_user_id_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id =request.session['logged_user_id']
        if inscription.objects.get(pk=logged_user_id)!=None:
            return inscription.objects.get(pk=logged_user_id) 
        else:
            return None
    else:
        return None

def detailmatiere(request,idpm):
    logged_user=get_logger_user_id_from_request(request)
    if logged_user:
        detailpm=get_object_or_404(profmatiere,idpm=idpm)
        return render(request,'detailmatiere.html',{'dtlpm':detailpm,'logged_user':logged_user})
    else:
        return redirect('connexion') 

def detailnotes(request,id):
    logged_user=get_logger_user_id_from_request(request)
    if logged_user:
        detailnote=get_object_or_404(notes,id=id)
        return render(request,'detailnote.html',{'dtlnote':detailnote,'logged_user':logged_user})
    else:
        return redirect('connexion') 

@api_view(['GET', 'POST', 'DELETE'])
def anneapi(request):
    if request.method=='GET':
        annee=anneeacademique.objects.all()
        serializer=anneeserialiser(annee,many=True) 
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        annee=JSONParser().parse(request)
        serializer=anneeserialiser(data=annee,many=True)
        if serializer.is_valid():
            serializer.save()      
            return JsonResponse('enregistrement avec succès',safe=False)
        return JsonResponse('echec d enregistrement123',safe=False)    


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
            return JsonResponse('enregistrement avec succès',safe=False)
        return JsonResponse('echec d enregistrement123',safe=False)    

    
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
          
        
@api_view(['GET', 'POST', 'DELETE'])     
def inscriptionapi(request):
    if request.method=='GET':
        inscript=inscription.objects.all()
        serializer=inscriptionserializer(inscript,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        inscript=JSONParser().parse(request)
        serializer=inscriptionserializer(data=inscript,many=True)
        if serializer.is_valid():
            serializer.save() 
            def controleutd(request):
                inscript=inscription.objects.all()
                for mon in inscript:
                    if mon.etudiant=='' or mon.formation=='' or mon.anneeacademique=='': 
                        if mon.etudiant=='':                       
                           etud=etudiant.objects.get(idetud=mon.idetud)
                           mon.etudiant=etud
                        if mon.formation=='':
                           format=formation.objects.get(idf=mon.idf)
                           mon.formation=format
                        if mon.anneeacademique=='':
                           annee=anneeacademique.objects.get(idan=mon.idan)  
                           mon.anneeacademique=annee
                        mon.save()                                           
            return JsonResponse('enregistrement avec succes',safe=False)
        return JsonResponse('echec',safe=False)            


@api_view(['GET', 'POST', 'DELETE'])     
def profmatiereapi(request):
    if request.method=='GET':
        matiere=profmatiere.objects.all()
        serializer=profmatiereserialiser (matiere,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        matiere=JSONParser().parse(request)
        serializer=profmatiereserialiser(data=matiere,many=True)
        if serializer.is_valid():
            serializer.save()
            def controlmatiere(request):
                mat=profmatiere.objects.all()
                if mat.formation=='':
                    format=formation.objects.get(idfor=mat.idfor)
                    mat.formation=format
                    mat.save()                    
            return JsonResponse('enregistrement avec succes',safe=False)
        return JsonResponse('echec',safe=False)          
        

            
                   
        
    
   
                