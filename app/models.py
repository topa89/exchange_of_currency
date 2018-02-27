from django.db import models


# Create your models here.

class limit_val(models.Model):
    index = models.CharField(max_length=10, verbose_name='Валюта')
    name = models.CharField(max_length=30, verbose_name='Название')
    reserve = models.DecimalField(default=1, max_digits=10, decimal_places=2, verbose_name='Резерв')
    min_val = models.DecimalField(default=1, max_digits=10, decimal_places=2, verbose_name='Мин знач')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = 'Резервы валюты'


class Order(models.Model):
    email= models.CharField(max_length=255, verbose_name='Email')


    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
