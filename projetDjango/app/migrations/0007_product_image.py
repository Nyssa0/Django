# Generated by Django 4.1.4 on 2022-12-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='Images', upload_to='Images'),
        ),
    ]
