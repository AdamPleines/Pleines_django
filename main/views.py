from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item, Product
from .forms import ProductForm

# Created views are below here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {"name":ls.name})

def home(response):
    return render(response, "main/home.html", {"name":"home"})

def about(response, *args, **kwargs):
    my_context = {
        "name":"about",
        "my_text": "This is my_text",
        "my_number": 1234,
        "my_list": [1313, 4231, 312, "Abcd"],
    }
    return render(response, "main/about.html", my_context)

def product_index(response, id):
    obj = Product.objects.get(id=id)
    # content = {
        # "name":"the product creation page",
        # "my_text": "This is my_text",
        # "my_number": 1234,
        # "my_list": [1313, 4231, 312, "Abcd"],
    # }
    prod_context = {
        'object': obj,
        "name": "product display",
    }
    return render(response, "main/product_detail.html", prod_context)

def product_detail(response, id):
    obj = Product.objects.get(id=id)
    # content = {
        # "name":"the product creation page",
        # "my_text": "This is my_text",
        # "my_number": 1234,
        # "my_list": [1313, 4231, 312, "Abcd"],
    # }
    prod_context = {
        'object': obj,
        "name": "product display",
    }
    return render(response, "main/product_detail.html", prod_context)

def product_new(response):
    if response.method == "POST":
        form = ProductForm(response.POST or None)
        if form.is_valid():
            form.save()
            # n = form.cleaned_data["title"]
            # t = ProductForm(title=n)
            # t.save()
            
    else:
        form = ProductForm()

    context = {
        'form': form,
        "name": "product creation",
    }
    return render(response, "main/product_new.html", context)

def v1(response):
    return HttpResponse("<h2>This is v1. I haven't really done anything here yet.</h2>")