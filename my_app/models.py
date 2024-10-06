from django.db import models

class Furniture(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    commit = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Tools(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    commit = models.TextField()

    def __str__(self) -> str:
        return self.name
    
