from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'app/home.html')

def user(request):
    # users = User.objects.all()
    # users = User.objects.filter(email="admin@gmail.com")
    # users = User.objects.filter(username="sulav")
    users = User.objects.filter(my_page__category = 'Programing')
    
    return render(request, 'app/user.html', {'users': users})

def page(request):
    page = Page.objects.all()
    # page = Page.objects.filter(category='Programing')
    # page = Page.objects.filter(user__username='priya')
    return render(request, 'app/page.html', {'page': page})


def post(request):
    # post = Post.objects.all()
    # post = Post.objects.filter(published='2025-12-16')
    post = Post.objects.filter(user__username='manita')
    return render(request, 'app/post.html', {'post': post})

def song(request):
    song = Song.objects.all()
    # song = Song.objects.filter(user__username='sulav')
    return render(request, 'app/song.html', {'song': song})
