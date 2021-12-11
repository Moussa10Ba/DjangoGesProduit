from django.db import models
from django.db.models.deletion import CASCADE
import datetime
# Create your models here.

class Categorie(models.Model):

    libelle = models.CharField(max_length=50)
     
    date_creation = models.DateField()
    
    def __str__(self):
       return self.libelle
   
    

class Produit(models.Model):

    libelle = models.CharField(max_length=30)
    quantite = models.IntegerField()
    reference =  models.CharField(max_length=30)
    categorie =  models.ForeignKey(Categorie, on_delete=CASCADE)