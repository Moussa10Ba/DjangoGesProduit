from django.urls import path
from django.urls.conf import include
from .import views
urlpatterns = [
  
    path('list/',views.produit_list,name='produit_list'),
    path('',views.produit_form,name='produit_add'),
    path('<int:id>/',views.produit_form, name='produit_update'),
    path('delete/<int:id>',views.produit_delete,name="produit_delete"),
    path('categorie/add',views.categorie_form,name="categorie_add"),
    path('categorie/list',views.categorie_list,name="categorie_list"),
    path('categorie/delete/<int:id>',views.categorie_delete,name="categorie_delete"),
    path('categorie/<int:id>',views.categorie_form,name="categorie_update")
]
