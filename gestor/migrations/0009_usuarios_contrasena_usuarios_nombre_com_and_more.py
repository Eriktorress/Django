# Generated by Django 4.0.5 on 2022-06-27 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0008_remove_usuarios_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='contrasena',
            field=models.CharField(blank=True, max_length=10, verbose_name='Contraseña'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='nombre_com',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombre completo'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='user',
            field=models.CharField(blank=True, max_length=100, verbose_name='Usuario'),
        ),
    ]
