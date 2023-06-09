# Generated by Django 4.2.1 on 2023-07-02 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreBodega', models.CharField(max_length=50)),
                ('direccionBodega', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Bodega',
                'verbose_name_plural': 'Bodegas',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoria', models.CharField(max_length=50)),
                ('descripcionCategoria', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('descripcionProducto', models.CharField(max_length=100)),
                ('bodega', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.bodega')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
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
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTienda', models.CharField(max_length=50)),
                ('direccionTienda', models.CharField(max_length=100)),
                ('bodega', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.bodega')),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
            },
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
                ('cantidadSalida', models.IntegerField()),
                ('fechaSalida', models.DateField()),
                ('descripcionSalida', models.CharField(max_length=100)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoBodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('id_Bodega', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.bodega')),
                ('id_Producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadEntrada', models.IntegerField()),
                ('fechaEntrada', models.DateField()),
                ('descripcionEntrada', models.CharField(max_length=100)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadDevolucion', models.IntegerField()),
                ('fechaDevolucion', models.DateField()),
                ('descripcionSalida', models.CharField(max_length=100)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.producto')),
            ],
        ),
    ]
