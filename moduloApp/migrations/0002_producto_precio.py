# Generated by Django 4.2.1 on 2023-07-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
