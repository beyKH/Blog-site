from django.shortcuts import render
from django.http import HttpResponse
from .models import  BlogPost


def index(request):
    post_list = BlogPost.objects.all()
    return render(request,"hfiles/index.html",{"blog_list":post_list[::-1]})

def about(request):
    return render(request,"hfiles/about.html",{"ism":"Asadbek"})