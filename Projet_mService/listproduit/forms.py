from django import forms
from .models import Produit, Categorie, ImageProduit

class ProduitForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput, required=False)

    class Meta:
        model = Produit
        fields = ['nom_produit', 'description', 'prix', 'quantite_stock', 'categorie']

    def __init__(self, *args, **kwargs):
        super(ProduitForm, self).__init__(*args, **kwargs)
        self.fields['categorie'].queryset = Categorie.objects.all()


class ImageProduitForm(forms.ModelForm):
    class Meta:
        model = ImageProduit
        fields = ['image']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'image']
