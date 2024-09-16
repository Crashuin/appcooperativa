# Generated by Django 5.0.6 on 2024-09-16 22:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oficinas',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('ubicación', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Asociado',
            fields=[
                ('cedula', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('estado_civil', models.CharField(max_length=20)),
                ('fecha_de_nacimiento', models.DateTimeField()),
                ('correo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=9)),
                ('estado', models.CharField(max_length=20)),
                ('sueldo', models.DecimalField(decimal_places=3, max_digits=10)),
                ('fecha_de_vinculación', models.DateTimeField(auto_now_add=True)),
                ('tipo_titularidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='album.asociado')),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_oficinas', to='album.oficinas')),
            ],
        ),
        migrations.CreateModel(
            name='Aportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=3, max_digits=10)),
                ('asociado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_asociados', to='album.asociado')),
            ],
        ),
    ]
