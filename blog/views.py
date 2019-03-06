from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.utils import timezone
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'blogs': blogs,
        'posts': posts
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
        return redirect('/blog/show/' + str(blog.id))

    
    return render(request, 'create.html')


def blogpost(request):
    if request.method == "POST":
        form = BlogForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/blog/show/' + str(post.id))
    else:
        form = BlogForm()
        return render(request, 'create.html', {'form': form})