from django.db import models

class User(models.Model):
    telegram_id = models.BigIntegerField(null=True, blank=True, unique=True)
    user_name = models.CharField(max_length=255)


class Category(models.Model):
    cat_name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Location(models.Model):
    loc_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255)


class Product(models.Model):
    product_name = models.CharField(max_length=255, default="Unknown")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField(null=True, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location_of_purchase = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='location_of_purchase')
    location_of_sale = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='location_of_sale')
    quantity_in_stock = models.PositiveIntegerField(default=0)
    quantity_in_delivery = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.user_name}'


class Photos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=255)
    upload_date = models.DateField()

