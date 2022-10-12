from django.db import models


class Investors(models.Model):
    name = models.CharField(max_length=60)
    address = models.TextField()
    credit = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
