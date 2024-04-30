from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_produit, name="list_produit"),  # URL pour la liste des produits
    path('add/', views.add_produit, name="add_produit"),  # URL pour ajouter un produit
    path('<int:produit_id>/', views.produit_detail, name="produit_detail"),  # URL pour les détails d'un produit
]
