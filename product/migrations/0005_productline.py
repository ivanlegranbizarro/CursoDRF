# Generated by Django 5.1 on 2024-08-24 08:51

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sku', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(100)])),
                ('stock_qty', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
