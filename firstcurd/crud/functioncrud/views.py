from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone
from .models import Blog
from .form import NewBlog

# Create your views here.
def welcome(request):
    return  render(request,'functioncrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'functioncrud/funccrud.html',{'blogs':blogs})
def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request,'functioncrud/new.html',{'form':form})
def update(request,pk):
    blog = get_object_or_404(Blog, pk = pk)
    form = NewBlog(request.POST, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'functioncrud/new.html', {'form': form})
def delete(request,pk):
    blog = get_object_or_404(Blog,pk = pk)
    blog.delete()
    return redirect('home')
