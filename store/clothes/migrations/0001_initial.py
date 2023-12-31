# Generated by Django 4.2.7 on 2023-11-11 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('desc', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('image', models.ImageField(upload_to='img/%Y/%m/%d/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='TypeOfClothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('desc', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('image', models.ImageField(upload_to='img/%Y/%m/%d/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Type of clothes',
                'verbose_name_plural': 'Types of clothing',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('desc', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('image', models.ImageField(upload_to='img/%Y/%m/%d/', verbose_name='Image')),
                ('fabric', models.CharField(max_length=100, verbose_name='Fabric type')),
                ('color', models.CharField(max_length=100, verbose_name='Color')),
                ('publication_date', models.DateTimeField(auto_now=True, verbose_name='Publication date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clothes.brand')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clothes.typeofclothing')),
            ],
            options={
                'verbose_name': 'Clothes',
                'verbose_name_plural': 'Clothes',
            },
        ),
    ]
