# Generated by Django 4.2.1 on 2023-07-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida_producto',
            name='fechaSalida',
            field=models.DateTimeField(),
        ),
    ]
