# Generated by Django 3.2.2 on 2021-05-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_dea', models.CharField(max_length=100)),
                ('direccion_ubicacion', models.CharField(max_length=100)),
                ('direccion_portal_numero', models.CharField(max_length=10)),
                ('horario_acceso', models.CharField(max_length=100)),
                ('x_utm', models.IntegerField(default=None)),
                ('y_utm', models.IntegerField(default=None)),
            ],
        ),
    ]
