from django.urls import path
from . import views

urlpatterns = [
    path('order/<int:item_id>/', views.order_item, name='order_item'),
]