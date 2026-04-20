from django.db import models
from products.models import Products


class Notification(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = "Notifications"
        ordering = ['-created_at']
