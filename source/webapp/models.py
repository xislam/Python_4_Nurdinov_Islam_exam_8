from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория')
    photo = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Фото')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        permissions = [
            ('can_have_piece_of_pizza', 'Может съесть кусочек пиццы'),
        ]


Rating_CHOICES = (
    (5, 'Суппер'),
    (4, 'Хороший'),
    (3, 'нормально'),
    (2, 'ну как то не тока с продуктом'),
    (1, 'атвратительный')
)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    rating = models.IntegerField(choices=Rating_CHOICES, verbose_name='Категория')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
