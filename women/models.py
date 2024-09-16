import uuid
from django.db import models
from django.contrib.auth.models import User


class Women(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItems(models.Model):
    cart = models.ForeignKey(
        Cart, blank=True, null=True, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        Women, blank=True, null=True, on_delete=models.CASCADE, related_name="cartitems"
    )
    quantity = models.IntegerField(default=0)


class WomenImage(models.Model):
    woman = models.ForeignKey(Women, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="img", default="", null=True, blank=True)

    def __str__(self):
        return self.name
