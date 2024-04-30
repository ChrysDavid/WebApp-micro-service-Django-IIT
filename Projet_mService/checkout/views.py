from django.shortcuts import render

# Create your views here.
def checkout(request):
    data = {}
    return render(request, 'checkout.html', data)