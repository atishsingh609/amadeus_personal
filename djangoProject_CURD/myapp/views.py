from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from unicodedata import category

from .models import Item, Category

# Create
def create_item(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        item = Item.objects.create(name=name, description=description)
        return redirect('list_items')
    return render(request, 'myapp/create_item.html')

# Read
def list_items(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})

# Update
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        return redirect('list_items')
    return render(request, 'myapp/update_item.html', {'item': item})

# Delete
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('list_items')
    return render(request, 'myapp/delete_item.html', {'item': item})


def get_item_per_category(request, pk):
    # category = get_object_or_404(Category, pk=pk)
    # item = category.items
    item = get_object_or_404(Item, pk=pk)
    cat = item.category_set.all()
    

