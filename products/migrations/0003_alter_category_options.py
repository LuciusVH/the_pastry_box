# Generated by Django 4.0.1 on 2022-01-27 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_brand_remove_product_id_remove_product_rating_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
