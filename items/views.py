from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from items.models import Item


from django.shortcuts import render
from .models import Item

def items_look(request):
    items = Item.objects.all()
    return render(request, 'items/items_look.html', {'items': items})
