from django.contrib import admin
from .models import (User,Restaurant,Option,MenuItem,Category,ItemCategory,Order,ItemOption,PromoCode,OrderCode,Address,OrderItem)
# Register your models here.

admin.site.register(User),
admin.site.register(Restaurant),
admin.site.register(Option),
admin.site.register(MenuItem),
admin.site.register(Category),
admin.site.register(ItemCategory),
admin.site.register(Order),
admin.site.register(ItemOption),
admin.site.register(PromoCode),
admin.site.register(OrderCode),
admin.site.register(Address),
admin.site.register(OrderItem),
