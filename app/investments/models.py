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


# id,investor_id,startup_name,invested_ammount,percentage_fees,date_added,fees_type
# 1,19,Aranda-Tamayo,81000,15,2021-01-15 15:38:21+00:00,upfront
