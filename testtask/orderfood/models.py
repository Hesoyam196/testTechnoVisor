from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):
    title = models.CharField(max_length=255)
    composition = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


class Order(models.Model):
    date = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk)


class DishOrder(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
