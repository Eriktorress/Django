# Generated by Django 4.0.5 on 2022-07-01 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0014_alter_usuarios_apelllidos_usu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesion',
            name='idprof',
        ),
    ]