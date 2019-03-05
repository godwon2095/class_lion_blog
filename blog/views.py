from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.utils import timezone

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'home.html', context)

def show(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'show.html', context)

def create(request):

    if request.method == "POST":
        blog = Blog()
        blog.title = request.POST.get('title')
        blog.body = request.POST.get('body')
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/show/' + str(blog.id))

    
    return render(request, 'create.html')