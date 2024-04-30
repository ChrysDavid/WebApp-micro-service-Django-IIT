from django.shortcuts import get_object_or_404, render, redirect
from .models import Produit, ImageProduit, Categorie
from .forms import ProduitForm, CategorieForm 
from django.contrib import messages


# Create your views here.
def list_produit(request):
    produits = Produit.objects.all()
    imageProduits = ImageProduit.objects.all()
    categories = Categorie.objects.all()
    data = {
        'produits':produits,
        'imageProduits':imageProduits,
        'categories':categories,
    }
    return render(request, 'produit-list-admin.html', data)


def produit_detail(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    images_produit = ImageProduit.objects.filter(produit=produit)
    categorie = get_object_or_404(Categorie, pk=produit.categorie_id)
    
    if request.method == "POST":
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit_detail', produit_id=produit_id)
    else:
        form = ProduitForm(instance=produit)
    
    data = {
        'produit': produit,
        'images_produit': images_produit,
        'categorie': categorie,
        'form': form,
    }
    return render(request, 'produit-detail-admin.html', data)




def add_produit(request):
    categories = Categorie.objects.all()
    
    if request.method == 'POST':
        produit_form = ProduitForm(request.POST, request.FILES)
        categorie_form = CategorieForm(request.POST, request.FILES)

        if produit_form.is_valid():
            produit = produit_form.save(commit=False)
            produit.administrateur = request.user
            produit.save()
            produit_form.save_m2m()  # Pour enregistrer la relation ManyToMany avec la catégorie
            images = request.FILES.getlist('images')
            for image in images:
                ImageProduit.objects.create(produit=produit, image=image)
            messages.success(request, "Le produit a été ajouté avec succès.")
            return redirect('list_produit')
        else:
            messages.error(request, "Le formulaire de produit n'est pas valide. Veuillez corriger les erreurs.")

        if categorie_form.is_valid():
            categorie = categorie_form.save()
            messages.success(request, "La catégorie a été ajoutée avec succès.")
            return redirect('add_produit')
        else:
            messages.error(request, "Le formulaire de catégorie n'est pas valide. Veuillez corriger les erreurs.")

    else:
        produit_form = ProduitForm()
        categorie_form = CategorieForm()

    return render(request, 'add-produit-admin.html', {'produit_form': produit_form, 'categorie_form': categorie_form, 'categories': categories})
