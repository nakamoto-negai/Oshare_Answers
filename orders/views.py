from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order
from items.models import Item

from django.contrib import messages
# ...existing code...

def order_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            quantity = form.cleaned_data['quantity']
            total_price = item.price * quantity

            # ポイント支払いの場合
            if payment_method.name == 'point':
                if request.user.points >= total_price:
                    request.user.points -= total_price
                    request.user.save()
                    Order.objects.create(
                        user=request.user,
                        item=form.cleaned_data['item'],
                        quantity=quantity,
                        payment_method=payment_method,
                        coupon=form.cleaned_data.get('coupon')
                    )
                    return redirect('order_complete')
                else:
                    messages.error(request, "ポイントが不足しています")
            else:
                Order.objects.create(
                    user=request.user,
                    item=form.cleaned_data['item'],
                    quantity=quantity,
                    payment_method=payment_method,
                    coupon=form.cleaned_data.get('coupon')
                )
                return redirect('order_complete')
    else:
        form = OrderForm(initial={'item': item})
    return render(request, 'orders/order_item.html', {'item': item, 'form': form})

def order_complete(request):
    return render(request, 'orders/order_complete.html')
# Create your views here.
