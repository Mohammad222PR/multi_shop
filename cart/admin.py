from django.contrib import admin
from .models import *
# Register your models here.


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','is_paid',)
    inlines = [OrderItemAdmin]
    list_filter = ('is_paid',)
