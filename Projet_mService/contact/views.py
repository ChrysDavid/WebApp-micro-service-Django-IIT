from django.shortcuts import render

# Create your views here.
def contact(request):
    data = {}
    return render(request, 'contact.html', data)

def confidentialite(request):
    data = {}
    return render(request, 'confidentialite.html', data)

def qui_somme_nous(request):
    data = {}
    return render(request, 'qui-somme-nous.html', data)