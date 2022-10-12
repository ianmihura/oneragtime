from django.db import models


class Cashcalls(models.Model):
    total_amount = models.IntegerField()
    credit = models.CharField(max_length=60)
    email_send = models.EmailField()
    date_added = models.DateTimeField()
    invoice_status = models.CharField(max_length=10)


# id,total_amount,IBAN,email_send,date_added,invoice_status
# 1,,,,,
