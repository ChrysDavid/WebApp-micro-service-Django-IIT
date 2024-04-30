from django.shortcuts import render

# Create your views here.
def home(request):
    datas = {}
    return render(request, "index.html", datas)