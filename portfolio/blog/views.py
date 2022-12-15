from django.shortcuts import render
from .models import *

def blog(request):
    objects = Blog.objects.all()
    context = {
        "objects": objects,
    }
    return render(request, "blog/blog.html", context)