from django.urls import path
from . import views

urlpatterns = [
   path('', views.List_blog, name="List_blog"),
   path('add_Post/', views.add_Post, name="add_Post"),
   path('<slug>/', views.post_detail, name="post_detail"),
   path('post/update/<int:post_id>/', views.update_post, name='update_post'),
   path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]