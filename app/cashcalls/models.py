from django.db import models


class Cashcalls(models.Model):
    total_amount = models.IntegerField()
    credit = models.TextField()
    email_send = models.EmailField()
    date_added = models.DateTimeField()
    invoice_status = models.CharField(max_length=10)
