from django.shortcuts import render

# Create your views here.
def elements(request):
    data = {}
    return render(request, 'elements.html', data)