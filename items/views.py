from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from items.models import Item

def order_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    # 注文フォームや処理をここに記述
    return render(request, 'orders/order_item.html', {'item': item})
# Create your views here.
