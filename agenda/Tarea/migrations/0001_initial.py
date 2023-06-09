# Generated by Django 4.2 on 2023-05-27 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('Descripcion', models.TextField(blank=True, null=True)),
                ('FechaInicio', models.DateField(default=datetime.date.today)),
                ('FechaFinalizacion', models.DateField(blank=True, null=True)),
                ('Prioridad', models.IntegerField(default=3)),
            ],
        ),
    ]
