# Generated by Django 5.0.3 on 2024-04-14 07:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(null=True)),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['client_name'],
                'indexes': [models.Index(fields=['client_name'], name='myapp_clien_client__cdba1c_idx'), models.Index(fields=['-reg_date'], name='myapp_clien_reg_dat_c59fb1_idx')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=250)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)])),
                ('prod_count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('append_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['prod_name'],
                'indexes': [models.Index(fields=['prod_name'], name='myapp_produ_prod_na_733566_idx'), models.Index(fields=['-append_date'], name='myapp_produ_append__345647_idx'), models.Index(fields=['price'], name='myapp_produ_price_e2ee0c_idx')],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now_add=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
                ('products', models.ManyToManyField(to='myapp.product')),
            ],
        ),
    ]
