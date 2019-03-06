from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=196)
    password = models.CharField(max_length=50)
