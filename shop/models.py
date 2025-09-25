from django.db import models
from django.conf import settings

if settings.USE_CLOUDINARY:
    from cloudinary.models import CloudinaryField
    IMAGE_FIELD = CloudinaryField('image')
else:
    IMAGE_FIELD = models.ImageField(upload_to='products/')

CATEGORY_CHOICES = [
    ('men', 'Men'),
    ('women', 'Women'),
    ('kid', 'Kid'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='men')
    image = IMAGE_FIELD
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
