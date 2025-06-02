from django.urls import path
from . import views

urlpatterns = [
    path('look/', views.items_look, name='items_look'),
    # 商品注文ページのURLも必要なら追加
    # path('order/<int:item_id>/', views.order_item, name='order_item'),
]