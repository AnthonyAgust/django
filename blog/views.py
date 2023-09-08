from django.shortcuts import render, get_object_or_404
from .models import Posts
# Create your views here.
def render_posts(request):

    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def posts_details(request, posts_id):
    posts = get_object_or_404(Posts, pk=posts_id)
    return render(request, 'post_detail.html', {"posts": posts})
