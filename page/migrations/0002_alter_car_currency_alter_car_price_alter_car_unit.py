# Generated by Django 5.1.4 on 2025-01-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='currency',
            field=models.CharField(default='AZN', max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='unit',
            field=models.CharField(default='KM', max_length=20),
        ),
    ]
