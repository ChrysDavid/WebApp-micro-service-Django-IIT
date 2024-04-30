from django.urls import path
from . import views

urlpatterns = [
   path('', views.contact, name="contact"),
   path('confidentialite/', views.confidentialite, name="confidentialite"),
   path('qui_somme_nous/', views.qui_somme_nous, name="qui_somme_nous"),
]