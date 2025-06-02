from django import forms
from django import forms
from items.models import Item
from payments.models import PaymentMethod
from coupons.models import Coupon  # Couponモデルが別アプリの場合

class OrderForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Item.objects.all(), label="商品")
    quantity = forms.IntegerField(min_value=1, label="数量")
    payment_method = forms.ModelChoiceField(queryset=PaymentMethod.objects.all(), label="決済方法")
    coupon = forms.ModelChoiceField(queryset=Coupon.objects.filter(active=True), label="クーポン", required=False)
