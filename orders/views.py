from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order
from items.models import Item

from django.contrib import messages
# ...existing code...

from items.models import Recommendation
from coupons.models import Coupon

def order_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        form.fields['coupon'].queryset = Coupon.objects.filter(users=request.user, active=True)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            quantity = form.cleaned_data['quantity']
            coupon = form.cleaned_data.get('coupon')
            total_price = item.price * quantity
            if coupon:
                # 例: coupon.discount_rate が 0.2 なら20%割引
                discount = total_price * coupon.discount
                total_price -= discount
            # --- おすすめ経由のクーポン付与処理 ---
            def give_coupon_if_recommended():
                try:
                    rec = Recommendation.objects.get(item=item, recommended_to=request.user)
                    if rec.recommended_from:
                        coupon = Coupon.objects.filter(active=True).first()
                        if coupon:
                            coupon.users.add(rec.recommended_from)
                except Recommendation.DoesNotExist:
                    pass
            # -----------------------------------

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
                    if coupon:
                        coupon.users.remove(request.user)
                    give_coupon_if_recommended()
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
                if coupon:
                    coupon.users.remove(request.user)
                give_coupon_if_recommended()
                return redirect('order_complete')
    else:
        form = OrderForm(initial={'item': item})
        form.fields['coupon'].queryset = Coupon.objects.filter(users=request.user, active=True)
    return render(request, 'orders/order_item.html', {'item': item, 'form': form})

def order_complete(request):
    return render(request, 'orders/order_complete.html')
# Create your views here.
