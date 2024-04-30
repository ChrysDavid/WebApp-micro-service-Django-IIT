from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')  # Obtenir le nom d'utilisateur du formulaire
            password = form.cleaned_data.get('password1')  # Obtenir le mot de passe du formulaire
            user = authenticate(request, username=username, password=password)  # Authentifier l'utilisateur
            if user is not None:
                login(request, user)  # Connecter l'utilisateur
                return redirect("index")
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {"form": form})
