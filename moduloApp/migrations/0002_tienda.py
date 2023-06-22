# Generated by Django 3.2.16 on 2023-06-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTienda', models.CharField(max_length=50)),
                ('direccionTienda', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
            },
        ),
    ]