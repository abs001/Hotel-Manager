from django.contrib import admin

from .models import MenuCategory, Menus, Tables, Order, OrderItem
admin.site.register(MenuCategory)
admin.site.register(Menus)
admin.site.register(Tables)
admin.site.register(Order)
admin.site.register(OrderItem)