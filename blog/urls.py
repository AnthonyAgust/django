from django.urls import path
from .views import render_posts, posts_details


app_name = 'blog'


urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:posts_id>', posts_details, name="posts_details"),
]
