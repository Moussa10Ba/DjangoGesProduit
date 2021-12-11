from django.shortcuts import redirect, render
from gesProduit.models import Categorie, Produit
from gesProduit.forms import CategorieForm, ProduitForm


# Create your views here.


def produit_list(request):
    context = {'produits' : Produit.objects.all()}
    return render(request,"produit_register/produit_list.html",context)


def produit_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = ProduitForm()
        else:
            produit = Produit.objects.get(pk=id)
            form = ProduitForm(instance=produit)
        return render(request,"produit_register/produit_form.html",{'form':form})
    else:
        if id == 0:
            form = ProduitForm(request.POST)
        else:
            produit = Produit.objects.get(pk=id)
            form = ProduitForm(request.POST,instance=produit)
        if form.is_valid():
            form.save()
        return redirect('/produit/list')

def produit_delete(request,id):
        produit = Produit.objects.get(pk=id)
        produit.delete()
        return redirect('/produit/list')

def categorie_form(request,id=0):
    if request.method == "GET": 
        if id == 0:
           cat_form = CategorieForm()
        else:
            categorie = Categorie.objects.get(pk=id)
            cat_form = CategorieForm(instance=categorie)
        return render(request,"categorie_register/categorie_form.html",{'cat_form': cat_form})
    else:
        if id == 0:
            cat_form = CategorieForm(request.POST)
        else:
            categorie = Categorie.objects.get(pk=id)
            cat_form = CategorieForm(request.POST,instance=categorie)
        if cat_form.is_valid():
            cat_form.save()           
        return redirect("/produit/categorie/list")
        
def categorie_list(request):
    context = {'categories':Categorie.objects.all()}
    return render(request,"categorie_register/categorie_list.html",context)

def categorie_delete(request,id):
    categorie = Categorie.objects.get(pk=id)
    categorie.delete()
    return redirect ('/produit/categorie/list')
