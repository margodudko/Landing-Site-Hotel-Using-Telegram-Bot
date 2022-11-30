from django.db import models


class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class PriceTable(models.Model):
    pc_title = models.CharField(max_length=200, verbose_name='Услуга')
    pc_old_price = models.CharField(max_length=200, verbose_name='Старая цена')
    pc_new_price = models.CharField(max_length=200, verbose_name='Цена')

    def __str__(self):
        return self.pc_title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
