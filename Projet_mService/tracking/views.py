from django.shortcuts import render

# Create your views here.
def tracking(request):
    data = {}
    return render(request, 'tracking.html', data)