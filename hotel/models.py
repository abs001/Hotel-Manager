from django.db import models


class Tables(models.Model):
    chairs = models.IntegerField()
    occupied = models.BooleanField(default=False)


class MenuCategory(models.Model):
    def __str__(self):
        return self.category
    category = models.TextField(max_length=100)


class Menus(models.Model):
    menu_name = models.TextField(max_length=200)
    menu_description = models.TextField()
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    menu_price = models.FloatField()


class Order(models.Model):
    table_number = models.ForeignKey(Tables, on_delete=models.CASCADE)
    order_amount = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class OrderItem(models.Model):
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.ForeignKey(Menus, on_delete=models.PROTECT)
    price = models.FloatField()
    qty = models.IntegerField()
    total_amount = models.FloatField()
