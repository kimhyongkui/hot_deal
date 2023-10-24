from django.db import models


class Fmkorea(models.Model):
    name = models.CharField(max_length=255)
    shop = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    deliver = models.CharField(max_length=45)


class Ppomppu(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=45)


class Ruliweb(models.Model):
    name = models.CharField(max_length=45)
