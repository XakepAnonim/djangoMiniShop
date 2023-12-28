from django.contrib.auth.models import User
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Проиводители'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    characteristics = models.TextField(verbose_name='Характеристики')
    description = models.TextField(verbose_name='Описание')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')
    picture = models.CharField(max_length=255, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.IntegerField(verbose_name='Количество')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
