from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.abstracts.models import AbstractBaseModel


class Address(AbstractBaseModel):
    street_name = models.CharField(max_length=50)
    home_number = models.IntegerField()

    def __str__(self):
        return self.street_name


class User(AbstractBaseModel):
    fullname = models.CharField(max_length=255)
    address = models.ForeignKey(Address, verbose_name=_("Address"), on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return self.fullname


class Restaurant(AbstractBaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MenuItem(AbstractBaseModel):
    restaurant = models.ForeignKey(Restaurant, verbose_name=_("Restaurant"), related_name="menu_items", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(AbstractBaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ItemCategory(AbstractBaseModel):
    menu_item = models.ForeignKey(MenuItem, verbose_name=_("Menu Item"), on_delete=models.CASCADE, related_name="categories")
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE, related_name="menu_items")

    def __str__(self):
        return f"{self.menu_item.name} - {self.category.name}"


ADD_ON_OR_VARIANT = [
    ("large", "Large"),
    ("extra cheese", "Extra cheese"),
]


class Option(AbstractBaseModel):
    name = models.CharField(max_length=50)
    add_or_no = models.CharField(max_length=50, choices=ADD_ON_OR_VARIANT, default="large")

    def __str__(self):
        return self.name


class ItemOption(AbstractBaseModel):
    menu_item = models.ForeignKey(MenuItem, verbose_name=_("Menu Item"), on_delete=models.CASCADE, related_name="options")
    option = models.ForeignKey(Option, verbose_name=_("Option"), on_delete=models.CASCADE, related_name="menu_items")
    price_delta = models.IntegerField()
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.menu_item.name} - {self.option.name}"


STATUS_CHOICES = [
    ("new", "New"),
    ("confirmed", "Confirmed"),
    ("delivering", "Delivering"),
    ("done", "Done"),
]


class PromoCode(AbstractBaseModel):
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code


class OrderCode(AbstractBaseModel):
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code


class Order(AbstractBaseModel):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name="orders")
    restaurant = models.ForeignKey(Restaurant, verbose_name=_("Restaurant"), on_delete=models.CASCADE, related_name="orders")
    address = models.ForeignKey(Address, verbose_name=_("Address"), on_delete=models.CASCADE, related_name="orders")
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="new")
    totals = models.IntegerField()
    promo_code = models.ManyToManyField(PromoCode, verbose_name=_("Promo Codes"), related_name="orders", blank=True)
    order_code = models.ManyToManyField(OrderCode, verbose_name=_("Order Codes"), related_name="orders", blank=True)

    def __str__(self):
        return f"Order {self.name} - {self.status}"


class OrderItem(AbstractBaseModel):
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.CASCADE, related_name="order_items")
    line_total = models.IntegerField()

    def __str__(self):
        return f"Item in {self.order.name}"