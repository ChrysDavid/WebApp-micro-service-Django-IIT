from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect")
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

    # data = {}
    # return render(request, 'login.html', data)

