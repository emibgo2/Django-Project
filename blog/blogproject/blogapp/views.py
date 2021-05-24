from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Blog

# 서버가 불러올때 어떤식으로 불러와서 보여줄건지를 지정

def home(request):
    blogs = Blog.objects # 쿼리셋
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'details': details})

def new(request):
    return  render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title= request.GET['title']
    blog.body= request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return  redirect('/blog:'+str(blog.id))