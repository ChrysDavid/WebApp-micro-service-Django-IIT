from django.shortcuts import render

# Create your views here.
def cart(request):
    data = {}
    return render(request, 'cart.html', data)