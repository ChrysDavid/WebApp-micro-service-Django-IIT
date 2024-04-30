from django.shortcuts import render

# Create your views here.
def dashboard(request):
    data = {}
    return render(request, 'vue_admin/dashboard.html', data)