# Generated by Django 4.2.7 on 2023-11-26 04:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('salas', '0003_rename_usuario_salas_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salas',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='salas',
            name='data_reserva',
        ),
        migrations.RemoveField(
            model_name='salas',
            name='data_solicitacao',
        ),
        migrations.RemoveField(
            model_name='salas',
            name='quem_reservou',
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateTimeField()),
                ('data_devolucao', models.DateTimeField()),
                ('data_solicitacao', models.DateField(default=datetime.date.today)),
                ('quem_reservou', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
                ('salas', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='salas.salas')),
            ],
            options={
                'verbose_name': 'Reserva',
            },
        ),
    ]
