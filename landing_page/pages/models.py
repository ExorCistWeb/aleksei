from django.db import models

# Create your models here.
class image(models.Model):
    data = models.DateTimeField(null=True,verbose_name='Название товара',)
    image = models.ImageField(blank=True, null=True,verbose_name='Название товара',)
    subject = models.TextField(max_length=500, verbose_name='Название товара',)
    text = models.TextField(max_length=500, verbose_name='Название товара',)

class Individual_consultation(models.Model):
    time = models.DecimalField(verbose_name='Название товара',)
    price = models.CharField(max_length=10,verbose_name='Название товара',)

class Family_consultation(models.Model):
    time = models.DecimalField(verbose_name='Название товара',)
    price = models.CharField(max_length=10, verbose_name='Название товара',)

class Consultation_subscription5(models.Model):
    time = models.DecimalField(
        verbose_name='Название товара',
        )
    price = models.CharField(
        max_length=10,
        verbose_name='Название товара',
        )
    discount = models.IntegerField(
        verbose_name=('Цена со скидкой'), 
        default=0
    )

class Consultation_subscription10(models.Model):
    time = models.DecimalField(
        verbose_name='Название товара',
        )
    price = models.CharField(
        max_length=10,verbose_name='Название товара',
        )
    discount = models.IntegerField(
        verbose_name=('Цена со скидкой'), 
        default=0
    )

class Consultation_subscription15(models.Model):
    time = models.DecimalField(
        verbose_name='Название товара',
        )
    price = models.CharField(
        max_length=10,verbose_name='Название товара',
        )
    discount = models.IntegerField(
        verbose_name=('Цена со скидкой'), 
        default=0
    )
    many = models.IntegerField(
        verbose_name=('Цена со скидкой'), 
        default=0,
    )
