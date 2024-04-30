from django.contrib import admin
from .models import Category, Post, Comment, Reaction, Image

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_date', 'category']
    prepopulated_fields = {'slug': ('title',)}  # Préremplir le champ slug avec le titre du post

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author', 'publication_date', 'post']

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ['reaction_type', 'author', 'post']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']
