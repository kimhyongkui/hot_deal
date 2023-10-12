from django.db import models


class Fmkorea(models.Model):
    name = models.CharField(max_length=255)
    shop = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10)
    deliver = models.CharField(max_length=255)

    class Meta:
        app_label = "hot_deal"


class Ppomppu(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    class Meta:
        app_label = "hot_deal"


class Ruliweb(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = "hot_deal"
