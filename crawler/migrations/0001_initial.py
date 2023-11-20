# Generated by Django 4.2.3 on 2023-11-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fmkorea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('shop', models.CharField(max_length=45)),
                ('price', models.CharField(max_length=45)),
                ('deliver', models.CharField(max_length=45)),
                ('date', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ppomppu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ruliweb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=30)),
            ],
        ),
    ]
