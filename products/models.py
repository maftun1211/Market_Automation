from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/" + str(self.name) + "/"

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/" + str(self.category.name) + "/"

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Products"


