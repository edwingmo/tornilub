# Generated by Django 4.0.3 on 2022-04-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_remove_favoritos_ip_remove_favoritos_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='favorito_status',
            field=models.BooleanField(default=False),
        ),
    ]
