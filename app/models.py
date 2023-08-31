from django.db import models


class ListData(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    class Meta:
        app_label = "hot_deal"

    def __str__(self):
        return self.name
