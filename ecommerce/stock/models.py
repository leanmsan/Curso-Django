from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    short_description = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    stock = models.IntegerField(default=20)

    def __str__(self):
        return self.name
    