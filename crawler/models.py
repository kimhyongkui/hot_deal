from django.db import models


class Fmkorea(models.Model):
    name = models.CharField(max_length=255)
    shop = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    deliver = models.CharField(max_length=45)
    date = models.CharField(max_length=45)
    url = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Ppomppu(models.Model):
    number = models.CharField(max_length=30, primary_key=True)
    category = models.CharField(max_length=45)
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=45)
    url = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Ruliweb(models.Model):
    number = models.CharField(max_length=30, primary_key=True)
    category = models.CharField(max_length=45)
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=45)
    url = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
