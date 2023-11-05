from django.db import models


class Fmkorea(models.Model):
    name = models.CharField(max_length=255)
    shop = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    deliver = models.CharField(max_length=45)
    url = models.CharField(max_length=255)


class Ppomppu(models.Model):
    category = models.CharField(max_length=45)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


class Ruliweb(models.Model):
    category = models.CharField(max_length=45)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
