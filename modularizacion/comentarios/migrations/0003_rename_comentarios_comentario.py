# Generated by Django 4.2 on 2023-04-25 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comentarios_fecha'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comentarios',
            new_name='Comentario',
        ),
    ]