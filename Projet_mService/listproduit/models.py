from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categorie_images')

    def __str__(self):
        return self.nom

class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom_produit = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_stock = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    administrateur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_produit

class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produit_images')

    def __str__(self):
        return f"Image de {self.produit.nom_produit}"
