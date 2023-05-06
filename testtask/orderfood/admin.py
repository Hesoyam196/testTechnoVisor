from django.contrib import admin
from orderfood.models import *


class DishAdmin(admin.ModelAdmin):
    list_display = ['id',  'title', 'price']
    search_fields = ['title', 'composition', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'employee', 'user']
    search_fields = ['date', 'employee', 'user']


class DishOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'dish']
    search_fields = ['order', 'dish']


admin.site.register(Employee)
admin.site.register(Dish, DishAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(DishOrder, DishOrderAdmin)