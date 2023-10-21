from django.db import models


class Fmkorea(models.Model):
    name = models.CharField(max_length=45)
    shop = models.CharField(max_length=45)
    price = models.IntegerField()
    deliver = models.CharField(max_length=45)

    class Meta:
        app_label = "hot_deal"


class Ppomppu(models.Model):
    name = models.CharField(max_length=45)
    category = models.CharField(max_length=45)

    class Meta:
        app_label = "hot_deal"


class Ruliweb(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        app_label = "hot_deal"
