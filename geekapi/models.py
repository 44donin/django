from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
