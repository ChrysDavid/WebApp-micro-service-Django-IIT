from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog, name="blog"),
   path('blog-details', views.blog_details, name="blog-details"),
   path('single-blog', views.single_blog, name="single-blog"),
]