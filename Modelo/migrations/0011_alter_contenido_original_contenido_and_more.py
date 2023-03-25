# Generated by Django 4.1.7 on 2023-03-25 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelo', '0010_alter_adjunto_imagen_alter_adjunto_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido_original',
            name='contenido',
            field=models.TextField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='contenido_original',
            name='fecha_acceso',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 3, 25, 20, 8, 25, 776706, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contenido_procesado',
            name='fecha_Creacion',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 3, 25, 20, 8, 25, 776706, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='fuente_informacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 3, 25, 20, 8, 25, 776706, tzinfo=datetime.timezone.utc)),
        ),
    ]
