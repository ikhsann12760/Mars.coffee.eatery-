from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Menu(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menus')
    price = models.DecimalField(max_digits=10, decimal_places=0) # Using 0 decimal places for Rupiah
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    is_highlight = models.BooleanField(default=False)

    def __str__(self):
        return self.name
