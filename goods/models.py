from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL категории')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        db_table = 'category'


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название товара')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL товара')
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение товара')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена товара')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория товара')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'product'
