# Generated by Django 5.1.4 on 2025-01-12 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
