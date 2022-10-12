from django.db import models


class Bills(models.Model):
    investor_id = models.IntegerField()
    investment_id = models.IntegerField(blank=True, null=True)
    fees_amount = models.DecimalField(max_digits=19, decimal_places=2)
    date_added = models.DateTimeField()
    fees_type = models.CharField(max_length=10)


# id,investor_id,investment_id,fees_amount,date_added,fees_type
# 1,,,0,,
