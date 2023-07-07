from django.db import models

# Create your models here.

class Size(models.Model):
    title = models.CharField(max_length=10)


    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=10)


    def __str__(self):
        return self.title
    

class Product(models.Model):
    PRODUCT_TYPE = [
        ('poshak','پوشاک'),
        ('electice','دوربین'),
        ('barghi','موبایل'),
        ('cafsh','کفش'),
        ('abajor','ابازور'),
        ('kerem','کرم'),
        ('saat','ساعت'),
        ('pahbad','پهباد'),
        
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000000)
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to='products/')
    size = models.ManyToManyField(Size, related_name='products', blank=True, null=True)
    color = models.ManyToManyField(Color, related_name='products',blank=True, null=True)
    product = models.CharField(choices=PRODUCT_TYPE, default='poshak',max_length=200)

    def __srt__(self):
        return self.title