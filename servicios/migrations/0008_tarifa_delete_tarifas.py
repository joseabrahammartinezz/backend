# Generated by Django 4.1.1 on 2022-10-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0007_tarifas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('cod_tarifa', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('monto_por_m3', models.FloatField()),
                ('porcentaje_m3', models.FloatField()),
                ('m3_inicio', models.FloatField()),
                ('m3_fin', models.FloatField()),
                ('monto_fijo', models.FloatField()),
            ],
            options={
                'db_table': 'tarifas',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Tarifas',
        ),
    ]
