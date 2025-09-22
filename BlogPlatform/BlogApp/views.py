from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'BlogApp/post_list.html', {'posts': posts})
