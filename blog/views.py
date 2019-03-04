from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'home.html', context)

def show(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, 'show.html', context)

def create(request):
    form = BlogForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('/show/' + str(form.instance.id))

    context = {
        'form': form
    }
    
    return render(request, 'create.html', context)