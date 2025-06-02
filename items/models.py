
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



class StockHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    change = models.IntegerField()  # プラスなら入庫、マイナスなら出庫
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    note = models.CharField(max_length=255, blank=True)

class Recommendation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='recommendations')
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE)
    recommended_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('item', 'recommended_by')  # 同じユーザーが同じ商品を複数回おすすめできないようにする

    def __str__(self):
        return f"{self.recommended_by.username} recommends {self.item.name}"
# Create your models here.
