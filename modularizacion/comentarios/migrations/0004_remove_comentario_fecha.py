# Generated by Django 4.2 on 2023-04-25 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_rename_comentarios_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='fecha',
        ),
    ]
