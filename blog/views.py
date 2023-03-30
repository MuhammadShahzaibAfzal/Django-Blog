from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-id')[:6]
    categories = Category.objects.all()
    context={
        'posts':posts,
        'categories':categories,
    }
    return render(request,'home.html',context)

def posts(request):
    searchtext = request.GET.get('searchtext')
    if searchtext is None:
        searchtext = ""

    
    posts = Post.objects.filter(Q(category__title__icontains=searchtext) | Q(title__icontains=searchtext)).order_by('-id')
    # paginator logics
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)



    categories = Category.objects.all()
    context={
        'posts':posts,
        'categories':categories,
        'page_obj':page_obj,
    }
    return render(request,'posts.html',context)



def post(request,pk):
    post = Post.objects.get(id=pk)
    categories = Category.objects.all()
    related_posts = Post.objects.filter(category__id=post.category.id)
    context={
        'post':post,
        'categories':categories,
        'related_posts':related_posts,
    }

    return render(request,'post.html',context)


def category(request,pk):
    category = Category.objects.get(id=pk)
    categories = Category.objects.all()
    posts = Post.objects.filter(category = category)
    posts_count = posts.count()
    context={
        'category':category,
        'categories':categories,
        'posts':posts,
        'posts_count':posts_count,
    }

    return render(request,'category.html',context)



def contactUs(request):
    if request.method=="POST":
        contact= Contact(name=request.POST['name'],email=request.POST['email'],message=request.POST['message'])
        contact.save()
        messages.success(request,"Message sent successfully!")
        return redirect("/contact-us/")

    categories = Category.objects.all()
    context={
        'categories':categories,
    }
    return render(request,'contact-us.html',context)


def aboutUs(request):
    categories = Category.objects.all()
    context={
        'categories':categories
    }
    return render(request,'about-us.html',context)