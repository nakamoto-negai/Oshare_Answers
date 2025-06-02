from django.db import models
class PaymentMethod(models.Model):
    METHOD_CHOICES = [
        ('point', 'ポイント支払い'),
       
        # 必要に応じて追加
    ]
    name = models.CharField(max_length=50, choices=METHOD_CHOICES, unique=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.get_name_display()
# Create your models here.
