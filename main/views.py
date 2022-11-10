from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {"name":ls.name})

def home(response):
    return render(response, "main/home.html", {"name":"home"})

def about(response, *args, **kwargs):
    my_context = {
        "name":"the about page",
        "my_text": "This is my_text",
        "my_number": 1234,
        "my_list": [1313, 4231, 312, "Abcd"],
    }
    return render(response, "main/about.html", my_context)

def v1(response):
    return HttpResponse("<h2>This is v1. I haven't really done anything here yet.</h2>")