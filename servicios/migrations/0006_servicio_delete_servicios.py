# Generated by Django 4.1.1 on 2022-09-26 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0005_alter_servicios_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('cod_servicio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('tarifa', models.CharField(max_length=255)),
                ('obs', models.CharField(blank=True, max_length=255, null=True)),
                ('multa_dia', models.FloatField()),
                ('tipo_cobro', models.CharField(choices=[('ex', 'EXTRA'), ('me', 'MENSUAL')], default='EXTRA', max_length=45)),
            ],
            options={
                'db_table': 'servicios',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='servicios',
        ),
    ]