
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Item(models.Model):
    # ...既存のフィールド...
    name = models.CharField(max_length=100)
    # 他のフィールド

class Recommendation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='recommendations')
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE)
    recommended_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('item', 'recommended_by')  # 同じユーザーが同じ商品を複数回おすすめできないようにする

    def __str__(self):
        return f"{self.recommended_by.username} recommends {self.item.name}"
# Create your models here.
