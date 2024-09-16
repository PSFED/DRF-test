from django.contrib import admin

from .models import Cart, CartItems, Women, Category

admin.site.register(Women)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItems)
