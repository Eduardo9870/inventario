# Generated by Django 3.2.16 on 2023-06-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0003_tienda_bodega'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDevolucion', models.CharField(max_length=50)),
                ('cantidadDevolucion', models.IntegerField()),
                ('precioDevolucion', models.IntegerField()),
                ('motivoDevolucion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Devolucion',
                'verbose_name_plural': 'Devoluciones',
            },
        ),
    ]
