# Generated by Django 4.2.3 on 2023-10-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fmkorea',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]