from django.urls import path
from . import views

urlpatterns = [
   path('', views.category, name="category"),
   path('', views.registration, name="registration"),
   path('', views.single_product, name="single-product"),
]