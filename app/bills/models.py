from django.db import models

# Create your models here.
class Bills(models.Model):
    investor_id = models.IntegerField()
    investment_id = models.IntegerField()
    fees_amount = models.IntegerField()
    date_added = models.DateField()
    fees_type = models.CharField(max_length=10)


# fk investor_id
# fk investment_id
# fees_type = [upfront, yearly]

# id,investor_id,investment_id,fees_amount,date_added,fees_type
# 1,,,0,,