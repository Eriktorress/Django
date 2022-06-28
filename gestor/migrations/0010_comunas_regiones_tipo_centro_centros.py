# Generated by Django 4.0.5 on 2022-06-28 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0009_usuarios_contrasena_usuarios_nombre_com_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Regiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_regi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tip_centr', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Centros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestor.comunas')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestor.regiones')),
                ('tipo_centro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestor.tipo_centro')),
            ],
        ),
    ]