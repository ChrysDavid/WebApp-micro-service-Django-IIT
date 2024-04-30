from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Category, Image
from .forms import PostForm, ImageForm

def delete_post(request, post_id):
    """
    Function to delete a blog post.

    Args:
        request (HttpRequest): The HTTP request object.
        post_id (int): The ID of the post to be deleted.

    Returns:
        HttpResponseRedirect: A redirect response to a suitable page (e.g., list of blogs).
    """
    
    # Get the post to delete
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('List_blog')  # Replace with the appropriate URL name
    else:
        # Display confirmation page or handle other non-POST requests (optional)
        return redirect('List_blog')  # Rediriger vers la liste des blogs si ce n'est pas une requête POST

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categories = Category.objects.all()  # Récupérer toutes les catégories
    images = Image.objects.filter(post=post)  # Récupérer les images de l'article concerné
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('post_detail' + str(post_id))
    else:
        form = PostForm(instance=post)
    
    return render(request, 'update_post.html', {'form': form, 'post_id': post_id, 'categories': categories, 'images': images})



def add_Post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            image_urls = request.FILES.getlist('images')
            for image_url in image_urls:
                image = Image(image=image_url, post=post)
                image.save()

            # Rediriger vers la page de détail du nouveau post
            return redirect('List_blog')

    else:
        post_form = PostForm()
        image_form = ImageForm()

    return render(request, 'vue_admin/add_post_admin.html', {'post_form': post_form, 'image_form': image_form})



def List_blog(request):
    posts = Post.objects.all()
    data = {'posts' : posts}
    return render(request, 'vue_admin/List_blog.html', data)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    data = {'post': post}
    return render(request, 'vue_admin/post-detail-admin.html', data)