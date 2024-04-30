from django.shortcuts import render

# Create your views here.
def confirmation(request):
    data = {}
    return render(request, 'confirmation.html', data)