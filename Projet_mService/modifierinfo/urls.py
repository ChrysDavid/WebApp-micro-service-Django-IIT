from django.urls import path
from . import views

urlpatterns = [
    path('', views.modifier_info, name="modifier_info"),  # URL pour la liste des produits
]
