
from django import forms
from django.forms import fields
from .models import Categorie, Produit

class ProduitForm(forms.ModelForm):

    class Meta:
        model = Produit
        fields = ('libelle','reference', 'quantite', 'categorie')
        labels = {
            'categorie' : 'Choisir Une Categorie',
            'libelle' : 'Libelle Du Produit'
        }

      
class CategorieForm(forms.ModelForm):
    class  Meta:
        model = Categorie
        fields = ('libelle','date_creation')  
        widgets = {
       'date_creation': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }             
    
       