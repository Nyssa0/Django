# Generated by Django 4.1.4 on 2022-12-16 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_description_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
