# Generated by Django 5.0 on 2023-12-27 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('characteristics', models.TextField()),
                ('description', models.TextField()),
                ('picture', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniShop.category')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniShop.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniShop.product')),
            ],
        ),
    ]
