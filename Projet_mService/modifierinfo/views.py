from django.shortcuts import render

# Create your views here.
def modifier_info(request):
    data = {}
    return render(request, 'vue_user/modifier-info.html')