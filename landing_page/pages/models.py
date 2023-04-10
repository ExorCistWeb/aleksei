from datetime import timezone
from django.db import models

# Create your models here.
class Image(models.Model):
    data = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    subject = models.TextField(max_length=500)
    text = models.TextField(max_length=500)

    def __str__(self) -> str:
        return str(self.image)

    class Meta:
        verbose_name = ('Слайдер')
        verbose_name_plural = ('Слайдер')  


class Post(models.Model):
    time = models.CharField(max_length=150)
    price = models.CharField(max_length=40)

    def __str__(self) -> str:
        return str(self.time)

    class Meta:
        verbose_name = ('Индивидуальная консультация')
        verbose_name_plural = ('Индивидуальная консультация')


class Subscription(models.Model):
    time = models.CharField(max_length=150, null=True, blank=True)
    price = models.CharField(max_length=40 , null=True, blank=True)
    text = models.TextField(max_length=100, null=True, blank=True)
    maney = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.time )
    
    class Meta:
        verbose_name = ('Абонемент 10 консультаций')
        verbose_name_plural = ('Абонемент 10 консультаций')

"""
class Individual(models.Model):
    time = models.CharField(max_length=140)
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )

    def __str__(self) -> str:
        return str(self.time)

    class Meta:
        verbose_name = ('Индивидуальная консультация')
        verbose_name_plural = ('Индивидуальная консультация')

class Family(models.Model):
    time = models.CharField(max_length=140)
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )

    def __str__(self) -> str:
        return str(self.time )

    class Meta:
        verbose_name = ('Семейная консультация')
        verbose_name_plural = ('Семейная консультация')

class Subscription5(models.Model):
    time = models.CharField(max_length=140)
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )
    discount = models.CharField(
        verbose_name=('Специальное предложение'), 
        default=0,
        max_length=140
    )

    class Meta:
        verbose_name = ('Абонемент 5 консультаций')
        verbose_name_plural = ('Абонемент 5 консультаций')

class Subscription10(models.Model):
    time = models.CharField(max_length=140)
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )
    discount = models.CharField(
        verbose_name=('Специальное предложение'), 
        default=0,
        max_length=140
    )

    def __str__(self) -> str:
        return str(self.time )
    
    class Meta:
        verbose_name = ('Абонемент 10 консультаций')
        verbose_name_plural = ('Абонемент 10 консультаций')

class Subscription15(models.Model):
    time = models.CharField(max_length=140)
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )
    discount = models.CharField(
        verbose_name=('Специальное предложение'), 
        default=0,
        max_length=140,
    )

    def __str__(self) -> str:
        return str(self.time )

    class Meta:
        verbose_name = ('Абонемент 15 консультаций')
        verbose_name_plural = ('Абонемент 15 консультаций')
"""
