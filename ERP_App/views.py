from django.shortcuts import render

# Create your views here.
from .models import *

from .forms import *

# def demo(request):
#     return render(request, 'books.html')


def index(request):
    if request.method == 'POST':
        add_item = ERP_Form(request.POST, request.FILES)
        if add_item.is_valid():
            add_item.save()
        add_cat = Category_Form(request.POST, request.FILES)
        if add_cat.is_valid():
            add_cat.save()
    categories = Category.objects.all()
    items = Item.objects.all()
    form = ERP_Form()
    form_cat = Category_Form()
    context = {"items": items, 'categories': categories,
               "form": form, "form_cat": form_cat}
    return render(request, 'home.html', context)


def items(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    context = {"items": items, 'categories': categories}
    return render(request, 'items.html', context)


def add_item(request):
    if request.method == 'POST':
        add = ERP_Form(request.POST, request.FILES)
        if add.is_valid():
            add.save()
    form = ERP_Form()
    context = {'form': form}
    return render(request, 'add.html', context)

#     return render(request, 'add.html')

# def update(request):
#     return render(request, 'update.html')

# def delete(request):
#     return render(request, 'delete.html')
