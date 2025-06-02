from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order
from items.models import Item

def order_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                user=request.user,
                item=form.cleaned_data['item'],
                quantity=form.cleaned_data['quantity'],
                payment_method=form.cleaned_data['payment_method'],
                coupon=form.cleaned_data.get('coupon')
            )
            return redirect('order_complete')
    else:
        form = OrderForm(initial={'item': item})
    return render(request, 'orders/order_item.html', {'item': item, 'form': form})

def order_complete(request):
    return render(request, 'orders/order_complete.html')
# Create your views here.
