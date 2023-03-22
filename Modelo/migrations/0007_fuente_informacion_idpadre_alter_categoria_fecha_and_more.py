# Generated by Django 4.1.7 on 2023-03-21 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelo', '0006_alter_contenido_original_fecha_acceso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuente_informacion',
            name='idPadre',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='fecha',
            field=models.DateField(default=datetime.date(2023, 3, 21)),
        ),
        migrations.AlterField(
            model_name='contenido_original',
            name='fecha_acceso',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 3, 21, 21, 39, 29, 773398, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contenido_procesado',
            name='fecha_Creacion',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 3, 21, 21, 39, 29, 774486, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='fuente_informacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 3, 21, 21, 39, 29, 773398, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Links',
        ),
    ]
