from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    STATUS_CHOICES = (
        ('lead', 'Lead'),
        ('contacted', 'Contacted'),
        ('converted', 'Converted'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='lead')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="customers/", blank=True, null=True)

    def __str__(self):
        return self.name
