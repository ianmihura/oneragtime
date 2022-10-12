from django.db import models


class Investments(models.Model):
    investor_id = models.IntegerField()
    # error: fk creates field investor_id_id in DB and model
    # investor_id = models.ForeignKey(
    #     Investors, related_name='pk', on_delete=models.CASCADE, db_column='investor_id')
    startup_name = models.CharField(max_length=60)
    invested_amount = models.IntegerField()
    percentage_fees = models.IntegerField()
    date_added = models.DateTimeField()
    fees_type = models.CharField(max_length=10)
