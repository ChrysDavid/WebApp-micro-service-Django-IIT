from django.shortcuts import render

# Create your views here.
def category(request):
    data = {}
    return render(request, 'category.html', data)

def registration(request):
    data = {}
    return render(request, 'registration.html', data)

def single_product(request):
    data = {}
    return render(request, 'single-product.html', data)