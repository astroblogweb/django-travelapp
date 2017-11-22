from django.db import models

class DataGen(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    keyword=models.CharField(max_length=50)
    # created = models.DateTimeField(auto_now_add=True)

# class PriceCompare(models.Model):
#     name=models.CharField(max_length=100)
#     price_amazon=models.DecimalField(blank=True)
#     price_flipkart=models.DecimalField(blank=True)
#     price_paytm=models.DecimalField(blank=True)