from django.shortcuts import render

# Create your views here.
def blog(request):
    data = {}
    return render(request, 'blog.html', data)

def blog_details(request):
    data = {}
    return render(request, 'blog-details.html', data)

def single_blog(request):
    data = {}
    return render(request, 'single-blog.html', data)
