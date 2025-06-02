from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order
from items.models import Item

def order_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            Order.objects.create(
                user=request.user,
                item=item,
                quantity=quantity
            )
            return redirect('order_complete')  # 完了ページへリダイレクト
    else:
        form = OrderForm()
    return render(request, 'orders/order_item.html', {'item': item, 'form': form})

def order_complete(request):
    return render(request, 'orders/order_complete.html')
# Create your views here.
