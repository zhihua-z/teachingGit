from django.shortcuts import render

from .models import User, Post

# Create your views here.
def index(request):
    # fetch all posts
    posts = Post.objects.all()

    for x in posts:
        x.display_time = '2d'

    context = {
        'post': posts,
    }

    return render(request, 'insta/index.html', context)