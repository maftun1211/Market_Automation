from django.db import models
from products.models import Products
from django.contrib.auth.models import User

class Stocklog(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='stock_logs')
    old_stock = models.PositiveIntegerField(default=0)
    new_stock = models.PositiveIntegerField(default=0)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.product.name} | {self.old_stock} | {self.new_stock}"

    class Meta:
        verbose_name_plural = "Stock Logs"

class Saleslog(models.Model):
    period = models.CharField(max_length=10,
                              choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')])
    total_sales = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f" {self.period} | {self.total_sales}"

    class Meta:
        verbose_name_plural = "Sales Logs"

class UserActivitylog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=10,
                                choices=[('login', 'Login'), ('logout', 'Logout'),('purchase', 'Purchase')])

    def __str__(self):
        return f" {self.user} | {self.activity}"

    class Meta:
        verbose_name_plural = "User Activity Logs"


