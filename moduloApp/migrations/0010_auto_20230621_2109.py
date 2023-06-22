# Generated by Django 3.2.16 on 2023-06-22 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0009_salida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRol', models.CharField(max_length=50)),
                ('descripcionRol', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='descripcion',
            new_name='descripcionCategoria',
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTrabajador', models.CharField(max_length=50)),
                ('contraseñaTrabajador', models.CharField(max_length=50)),
                ('rol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.rol')),
                ('tienda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.tienda')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
        ),
        migrations.CreateModel(
            name='Salida_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSalida', models.DateField()),
                ('descripcionSalida', models.CharField(max_length=100)),
                ('bodega', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.bodega')),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDevolucion', models.DateField()),
                ('descripcionSalida', models.CharField(max_length=100)),
                ('bodega', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.bodega')),
            ],
        ),
    ]
