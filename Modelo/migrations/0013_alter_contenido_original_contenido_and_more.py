# Generated by Django 4.1.7 on 2023-03-25 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelo', '0012_alter_contenido_original_fecha_acceso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido_original',
            name='contenido',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contenido_original',
            name='fecha_acceso',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 3, 25, 20, 21, 16, 415769, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contenido_procesado',
            name='fecha_Creacion',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 3, 25, 20, 21, 16, 415769, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='fuente_informacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 3, 25, 20, 21, 16, 415769, tzinfo=datetime.timezone.utc)),
        ),
    ]
