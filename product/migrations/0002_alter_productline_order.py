# Generated by Django 5.1 on 2024-08-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productline',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
