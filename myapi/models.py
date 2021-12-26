from django.db import models

# Create your models here.


class Category(models.Model):
    #category_id = models.Index()
    name = models.CharField(max_length=60)
    total_sales = models.IntegerField(max_length=100)
    target_sales = models.IntegerField(max_length=100)
    state =models.CharField(max_length=60)
    def __str__(self):
        return self.name