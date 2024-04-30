from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.utils.text import slugify  # Importez la fonction slugify pour générer le slug

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/blog/category_images/')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  # Ajoutez le champ slug
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pre_save(self):
        # Générez le slug à partir du titre du post
        self.slug = slugify(self.title)

    def save(self, *args, **kwargs):
        self.pre_save()  # Appel de la méthode pre_save avant la sauvegarde
        super().save(*args, **kwargs)


class Comment(models.Model):
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)  # Utilisation de timezone.now() comme valeur par défaut
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Reaction(models.Model):
    LIKE = 'Like'
    DISLIKE = 'Dislike'
    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    reaction_type = models.CharField(max_length=7, choices=REACTION_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reaction_type} on {self.post.title}"

class Image(models.Model):
    image = models.ImageField(upload_to='img/blog/post_images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.image)
