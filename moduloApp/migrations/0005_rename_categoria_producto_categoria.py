# Generated by Django 3.2.19 on 2023-06-20 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0004_producto_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='Categoria',
            new_name='categoria',
        ),
    ]