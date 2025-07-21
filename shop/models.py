from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('kid', 'Kid'),
]

class Product(models.Model):
   
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.CharField(max_length=20, blank=True, null=True)  # 👈 NEW FIELD
    category = models.CharField(max_length=10,choices=CATEGORY_CHOICES,default='men') # CREATES DROPDOWN
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name
