# Generated by Django 4.2 on 2023-04-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0004_remove_comentario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]