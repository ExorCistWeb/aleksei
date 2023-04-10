from datetime import timezone
from django.db import models

# Create your models here.
class image(models.Model):
    data = models.DateTimeField(null=True)
    image = models.ImageField(blank=True, null=True)
    subject = models.TextField(max_length=500)
    text = models.TextField(max_length=500)

    class Meta:
        verbose_name = ('Слайдер')
        verbose_name_plural = ('Слайдер')

class Individual_consultation(models.Model):
    time = models.TimeField()
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )
    class Meta:
        verbose_name = ('Индивидуальная консультация')
        verbose_name_plural = ('Индивидуальная консультация')

class Family_consultation(models.Model):
    time = models.TimeField()
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )
    class Meta:
        verbose_name = ('Семейная консультация')
        verbose_name_plural = ('Семейная консультация')

class Consultation_subscription5(models.Model):
    time = models.TimeField()
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )
    discount = models.IntegerField(
        verbose_name=('Специальное предложение'), 
        default=0
    )
    is_discount = models.BooleanField(
        verbose_name=('Цена по скидке?'), 
        default=False
    )
    class Meta:
        verbose_name = ('Абонемент 5 консультаций')
        verbose_name_plural = ('Абонемент 5 консультаций')


        
class Consultation_subscription10(models.Model):
    time = models.TimeField()
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )
    discount = models.IntegerField(
        verbose_name=('Специальное предложение'), 
        default=0
    )    
    is_discount = models.BooleanField(
        verbose_name=('Цена по скидке?'), 
        default=False
    )
    class Meta:
        verbose_name = ('Абонемент 10 консультаций')
        verbose_name_plural = ('Абонемент 10 консультаций')

class Consultation_subscription15(models.Model):
    time = models.TimeField()
    price = models.IntegerField(
        verbose_name=('Цена'), 
        default=0
    )
    discount = models.IntegerField(
        verbose_name=('Специальное предложение'), 
        default=0
    )
    is_discount = models.BooleanField(
        verbose_name=('Цена по скидке?'), 
        default=False
    )
    class Meta:
        verbose_name = ('Абонемент 15 консультаций')
        verbose_name_plural = ('Абонемент 15 консультаций')
