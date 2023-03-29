# Generated by Django 4.1.7 on 2023-03-29 05:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelo', '0014_alter_categoria_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjunto',
            name='URL',
            field=models.URLField(blank=None, default='/home', unique=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='fecha',
            field=models.DateField(default=datetime.date(2023, 3, 29)),
        ),
        migrations.AlterField(
            model_name='contenido_original',
            name='fecha_acceso',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 3, 29, 5, 17, 5, 427727, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contenido_procesado',
            name='fecha_Creacion',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 3, 29, 5, 17, 5, 428724, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='fuente_informacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 3, 29, 5, 17, 5, 426730, tzinfo=datetime.timezone.utc)),
        ),
    ]
