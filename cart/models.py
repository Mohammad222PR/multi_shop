from django.db import models
from account.models import User
from product.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    quantity = models.IntegerField()
    price = models.PositiveBigIntegerField()

    

