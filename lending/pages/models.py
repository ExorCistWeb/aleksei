# Create your models here.
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
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=150)
    price = models.CharField(max_length=40)
    text = models.TextField(null=True, blank=True, max_length=100)
    @classmethod
    def create(cls, time ):
        post  = cls( time = time)

        return post 
        
    def __str__(self) -> str:
        return str(self.time)

    class Meta:
        verbose_name = ('Индивидуальная консультация')
        verbose_name_plural = ('Индивидуальная консультация')


class Subscription(models.Model):
    title1 = models.CharField(max_length=100)
    time = models.CharField(max_length=150)
    price1 = models.CharField(max_length=40 )
    text = models.TextField(max_length=100)
    maney = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.time )
    
    class Meta:
        verbose_name = ('Абонемент 10 консультаций')
        verbose_name_plural = ('Абонемент 10 консультаций')