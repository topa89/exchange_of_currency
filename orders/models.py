from django.db import models


class Orders(models.Model):
    email= models.EmailField()
    card_number = models.CharField(max_length=20, verbose_name=u'Номер карты')
    input_val = models.CharField(max_length=20, verbose_name=u'Валюта приема')
    output_val = models.CharField(max_length=20, verbose_name=u'Валюта отдачи')
    sum_from = models.CharField(max_length=10, verbose_name=u'Сумма приема')
    sum_to = models.CharField(max_length=10, verbose_name=u'Сумма отдачи')

    def __str__(self):
        return '{}, {} -> {}'.format(self.email , self.input_val, self.output_val)
    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'