from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
from .form import BlogPost
# 서버가 불러올때 어떤식으로 불러와서 보여줄건지를 지정

def home(request):
    blogs = Blog.objects # 쿼리셋
    return render(request,'home.html',{'blogs':blogs})

def map(request):
    return  render(request,'map.html')

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

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기술 -> POST
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})
