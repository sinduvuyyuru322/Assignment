# Generated by Django 5.1.3 on 2024-11-14 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demartapp', '0004_rename_product_id_customer_details_customer_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_details',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='product_id',
        ),
    ]
