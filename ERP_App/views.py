from django.shortcuts import render

# Create your views here.
from .models import *

# def demo(request):
#     return render(request, 'books.html')


def index(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    context = {"items": items, 'categories': categories}
    return render(request, 'home.html', context)


def items(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    context = {"items": items, 'categories': categories}
    return render(request, 'items.html', context)

# def update(request):
#     return render(request, 'update.html')

# def delete(request):
#     return render(request, 'delete.html')
