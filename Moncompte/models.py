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
    idfor=models.IntegerField()
    campus=models.CharField(max_length=40,null=True,blank=True)
    domain=models.CharField(max_length=50,null=True,blank=True)
    filiere=models.CharField(max_length=50,null=True,blank=True)
    detailformation=models.CharField(max_length=50,null=True,blank=True)
    periode=models.CharField(max_length=50,null=True,blank=True)
    niveau=models.CharField(max_length=50,null=True,blank=True)
    cycle=models.CharField(max_length=50,null=True, blank=True)
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
    idetud=models.IntegerField()
    class meta():
        verbose_name='etudiant'
    def __str__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse(etudiant, kwargs={"pk": self.pk})
    
class anneeacademique(models.Model):
    libelle=models.CharField(max_length=10)
    idan=models.IntegerField(default=1)
    class meta ():
        ordering=['an_libelle']
        verbose_name='anneeacademique'
    def __str__(self):
        return self.libelle
    def get_absolute_url(self):
        return reverse(anneeacademique, kwargs={"pk": self.pk})
        
class profmatiere(models.Model):
    formationpm=models.ForeignKey(formation, verbose_name=("formation"), on_delete=models.CASCADE,null=True, blank=True)
    # formasem vient une fois avec dans la requette des profmat
    semestre=models.CharField(max_length=50)
    idsem=models.IntegerField()    
    # ajout des formasue aussi dans la requette 
    ue=models.CharField(max_length=50)    
    codeue=models.CharField(max_length=15,null=True, blank=True)
    creditue=models.IntegerField()
    moduleue=models.CharField(max_length=50,null=True, blank=True)
    idue=models.IntegerField()
    idfor=models.IntegerField()    
   # ajout maintenant de la profmat 
    matiere=models.CharField(max_length=50)
    enseignant=models.CharField(max_length=50,null=True, blank=True)  
    creditpm=models.IntegerField()
    codepm=models.CharField(max_length=15,null=True, blank=True)
    idpm=models.IntegerField()
    
    class meta():
        verbose_name='profmatiere'
    def __str__(self):
        return self.codepm
    def get_absolute_url(self):
        return reverse(profmatiere, kwargs={"pk": self.pk})
    
class emplois_de_temps(models.Model):
    jour=models.CharField(max_length=10)
    idem=models.IntegerField()
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
    idins=models.IntegerField() 
    idf=models.IntegerField()  
    idfor=models.IntegerField() 
    idan=models.IntegerField()
    etudiant=models.ForeignKey(etudiant, on_delete=models.CASCADE,related_name="etudiant",null=True)  
    anneeacademique=models.ForeignKey(anneeacademique, verbose_name=("anneeacademique"), on_delete=models.CASCADE,null=True)
    formationins=models.ForeignKey(formation, verbose_name=("formation"), on_delete=models.CASCADE,null=True) 
    inslogin=models.CharField(max_length=50,null=True)    
    insmdp=models.CharField(max_length=50,null=True)
    tof=models.ImageField(null=True, blank=True)
    class meta():
        verbose_name='inscription'
    def __str__(self):
        return self.inslogin
    def get_absolute_url(self):
         return reverse(inscription, kwargs={"pk": self.pk})
     
class notes(models.Model):
    idpm=models.IntegerField()
    idins=models.IntegerField()
    moyesem=models.DecimalField(max_digits=2,decimal_places=2)
    moyue=models.DecimalField(max_digits=2,decimal_places=2)
    moypm=models.DecimalField(max_digits=2,decimal_places=2)
    creditsem=models.IntegerField()
    creditue=models.IntegerField()
    creditpm=models.IntegerField()
    decisionsem=models.CharField(max_length=10)
    decisionue=models.CharField(max_length=10)
    decisionpm=models.CharField(max_length=10)
    sessionsem=models.CharField(max_length=15)
    sessionue=models.CharField(max_length=15)
    sessionpm=models.CharField(max_length=15)    
    profmatiere=models.ForeignKey(profmatiere, verbose_name=("profmatiere"), on_delete=models.CASCADE)    
    inscription=models.ForeignKey(inscription, verbose_name=("inscription"), on_delete=models.CASCADE)  
    class meta ():
        verbose_name='notesemestre'  
    def __str__(self):
        return self.ancienid
    def get_absolute_url(self):
         return reverse(notes, kwargs={"pk": self.pk})


    
            
         
