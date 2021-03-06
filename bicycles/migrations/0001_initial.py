# Generated by Django 3.1.5 on 2021-01-28 19:38

import bicycles.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike_brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('categories_bicycles', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bike_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('categories_bicycles', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductBicycles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50, unique=True)),
                ('titel_model', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('images', models.ImageField(upload_to=bicycles.models.ProductBicycles.get_file_name_bicycles)),
                ('description', models.CharField(max_length=300, null=True)),
                ('bike_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bicycles.bike_brand')),
                ('bike_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bicycles.bike_type')),
            ],
        ),
    ]
