# Generated by Django 4.2 on 2023-04-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('subject', models.TextField(max_length=500)),
                ('text', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдер',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=40)),
                ('text', models.TextField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Индивидуальная консультация',
                'verbose_name_plural': 'Индивидуальная консультация',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.CharField(blank=True, max_length=40, null=True)),
                ('text', models.TextField(blank=True, max_length=100, null=True)),
                ('maney', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Абонемент 10 консультаций',
                'verbose_name_plural': 'Абонемент 10 консультаций',
            },
        ),
    ]