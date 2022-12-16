from django.shortcuts import render, get_object_or_404
from .models import *

def blog(request):
    objects = Blog.objects.all()
    context = {
        "objects": objects,
    }
    return render(request, "blog/blog.html", context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/deteil.html',{'blog': blog})