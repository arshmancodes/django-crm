from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def blogs_view(request, *args, **kwargs):
    return render(request, "blogs.html", {})
