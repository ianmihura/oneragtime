from django.db import models

# Create your models here.
class Cashcalls(models.Model):
    total_amount = models.IntegerField()
    IBAN = models.CharField(max_length=60)
    email_send = models.EmailField()
    date_added = models.DateField()
    invoice_status = models.CharField(max_length=10)


# id,total_amount,IBAN,email_send,date_added,invoice_status
# 1,,,,,

# TODO invoice_status = [valid, sent, paid, overdue]