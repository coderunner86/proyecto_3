# Generated by Django 5.0.6 on 2024-05-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('pendiente', 'pendiente'), ('en progreso', 'en progreso'), ('completada', 'completada')], max_length=20)),
            ],
        ),
    ]
