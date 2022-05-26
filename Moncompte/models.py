from ast import Return
from pickle import TRUE
from sre_parse import Verbose
from django.db import models
from django.urls import reverse

# Create your models here.
class formation(models.Model):
    libelle=models.CharField(max_length=50)
    tutelle=models.CharField(max_length=50,null=True,blank=True)
    parcours=models.CharField(max_length=50,null=True,blank=True)
    ancien_idfor=models.IntegerField()
    campus=models.CharField(max_length=40,null=True,blank=True)
    domain=models.CharField(max_length=50,null=True,blank=True)
    filiere=models.CharField(max_length=50,null=True,blank=True)
    detailformation=models.CharField(max_length=50,null=True,blank=True)
    periode=models.CharField(max_length=50,null=True,blank=True)
    niveau=models.CharField(max_length=50,null=True,blank=True)
    idf=models.IntegerField()    
    class meta():
        verbose_name='formation'
        ordering=['for_libelle']
    def __str__(self):
        return self.libelle
    def get_absolute_url(self):
        return reverse(formation, kwargs={"pk": self.pk})
    
class etudiant(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50,null=True, blank=True) 
    date=models.CharField(max_length=50,null=True, blank=True)  
    lieu=models.CharField(max_length=50,null=True, blank=True)
    ancienid=models.IntegerField()
    class meta():
        verbose_name='etudiant'
    def __str__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse(etudiant, kwargs={"pk": self.pk})
    
class anneeacademique(models.Model):
    libelle=models.CharField(max_length=10)
    ancienid=models.IntegerField()
    class meta ():
        ordering=['an_libelle']
        verbose_name='anneeacademique'
    def __str__(self):
        return self.libelle
    def get_absolute_url(self):
        return reverse(anneeacademique, kwargs={"pk": self.pk})
class formasem (models.Model):
    semestre=models.CharField(max_length=50)
    cycle=models.CharField(max_length=50,null=True, blank=True)
    niveau=models.CharField(max_length=50,null=True, blank=True)
    ancienid=models.IntegerField()
    formation=models.ForeignKey(formation, verbose_name=("formation"), on_delete=models.CASCADE,null=True, blank=True)
    class meta():
        verbose_name='formasem'    
    def __str__(self):
        return self.semestre    
    def get_absolute_url(self):
        return reverse(formasem, kwargs={"pk": self.pk})
    
class formasue (models.Model):
    ue=models.CharField(max_length=50)    
    codeue=models.CharField(max_length=15,null=True, blank=True)
    creditue=models.IntegerField()
    moduleue=models.CharField(max_length=50,null=True, blank=True)
    ancienid=models.IntegerField()
    formasem=models.ForeignKey(formasem, on_delete=models.CASCADE,null=True, blank=True)    
    class meta():
        verbose_name="formasue"        
    def __str__(self):
        return self.ue 
    def get_absolute_url(self):
        return reverse(formasue, kwargs={"pk": self.pk})
    
class profmatiere(models.Model):
    matiere=models.CharField(max_length=50)
    enseignant=models.CharField(max_length=50,null=True, blank=True)  
    creditpm=models.IntegerField()
    codepm=models.CharField(max_length=15,null=True, blank=True)
    ancienid=models.IntegerField()
    formasue=models.ForeignKey(formasue, on_delete=models.CASCADE,null=True, blank=True)
    class meta():
        verbose_name='profmatiere'
    def __str__(self):
        return self.codepm
    def get_absolute_url(self):
        return reverse(profmatiere, kwargs={"pk": self.pk})
    
class emplois_de_temps(models.Model):
    jour=models.CharField(max_length=10)
    ancienid=models.IntegerField()
    hd=models.TimeField(null=True,blank=True)
    hf=models.TimeField(null=True,blank=True)
    profmatiere=models.ForeignKey(profmatiere, verbose_name=("profmatiere"), on_delete=models.CASCADE,null=True, blank=True)
    anneeacademique=models.ForeignKey(anneeacademique, verbose_name=("anneeacademique"), on_delete=models.CASCADE,null=True, blank=True)
    class meta():
        verbose_name='emplois_de_temps'
    def __str__(self):
        return self.jour
    def get_absolute_url(self):
         return reverse(emplois_de_temps, kwargs={"pk": self.pk})
     
     
class inscription(models.Model):
    ancienid=models.IntegerField(blank=True,null=True)   
    etudiant=models.ForeignKey(etudiant, on_delete=models.CASCADE,related_name="etudiant",null=True)  
    anneeacademique=models.ForeignKey(anneeacademique, verbose_name=("anneeacademique"), on_delete=models.CASCADE,related_name="anneeacademique",null=True)
    formation=models.ForeignKey(formation, verbose_name=("formation"), on_delete=models.CASCADE,related_name="formation",null=True) 
    inslogin=models.CharField(max_length=50,null=True)
    idf=models.IntegerField(blank=True,null=TRUE)
    insmdp=models.CharField(max_length=50,null=True)
    class meta():
        verbose_name='inscription'
    def __str__(self):
        return self.inslogin
    def get_absolute_url(self):
         return reverse(inscription, kwargs={"pk": self.pk})
     
class notesemestre(models.Model):
    ancienid=models.IntegerField()
    moyenne=models.DecimalField(max_digits=2,decimal_places=2)
    creditsem=models.IntegerField()
    decision=models.CharField(max_length=10)
    session=models.CharField(max_length=15)
    formasem=models.ForeignKey(formasem, verbose_name=("formasem"), on_delete=models.CASCADE)    
    inscription=models.ForeignKey(inscription, verbose_name=("inscription"), on_delete=models.CASCADE)  
    class meta ():
        verbose_name='notesemestre'  
    def __str__(self):
        return self.ancienid
    def get_absolute_url(self):
         return reverse(notesemestre, kwargs={"pk": self.pk})
     

    
            
         
