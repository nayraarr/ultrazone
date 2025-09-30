import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('footwear', 'Footwear'),
        ('scarf', 'Scarf'),
        ('jacket', 'Jacket'),
        ('hat', 'Hat'),
        ('accessories', 'Accessories'),
    ]
    
    # nama, harga, deskripsi, thumbnail, kategori, is_featured, brand, rating
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='accessories')
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=20)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

