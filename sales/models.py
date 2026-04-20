from django.db import models

from products.models import Products


class Sale(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,
                              choices=[('pending','Pending'),('paid','Paid'),('cancelled','Cancelled')] )
    payment_method = models.CharField(max_length=100,
                                      choices=[('cash','Cash'),('card','Card')] )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Sales"

class SaleItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x  {self.quantity}"

    class Meta:
        verbose_name_plural = "Sale Items"



