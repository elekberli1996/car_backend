# Generated by Django 5.1.4 on 2025-01-13 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('part_name', models.CharField(max_length=50)),
                ('cond', models.CharField(default='Yeni', max_length=50)),
                ('price', models.IntegerField(null=True)),
                ('currency', models.CharField(default='AZN', max_length=20)),
                ('information', models.CharField(max_length=400)),
                ('name', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('main_img', models.ImageField(blank=True, upload_to='main_part_images/')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='other_part_images/')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='spareparts.parts')),
            ],
        ),
    ]
