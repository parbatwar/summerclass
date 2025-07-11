from django.db import models
from django.utils import timezone

class Category (models.Model):
  name = models. CharField(max_length=255)

  def __str__(self):
    return self.name
  

class Product (models.Model):
  name = models.CharField(max_length=100)
  price = models.FloatField()
  description = models.TextField()
  stock = models.IntegerField(default=1)
  status = models.BooleanField(default=0)
  category = models.ForeignKey(Category, on_delete=models. CASCADE)
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name