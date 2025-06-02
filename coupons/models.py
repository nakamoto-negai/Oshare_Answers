from django.db import models
from django.conf import settings

class Coupon(models.Model):

    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # 割引率や金額
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="coupons")

    def __str__(self):
        return self.code
# Create your models here.
