from django.db import models


class Investors(models.Model):
    name = models.CharField(max_length=60)
    address = models.TextField()
    credit = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()


# id,name,adress,credit,phone,email
# 1,
# Segismundo Marquez Casas,
# "Via Jose Angel Ballester 77 Álava, 64116",
# "Mastercard Dora Valdés 5594099635534392 05/25 CVV: 553",
# +34 748 83 32 19,
# segismundo_marquez_casas@fakeemail.com
