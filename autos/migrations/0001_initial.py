# Generated by Django 4.1 on 2022-08-22 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'db_table': 'marca',
            },
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('color', models.CharField(max_length=100, verbose_name='Color')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.marca')),
            ],
            options={
                'db_table': 'auto',
            },
        ),
    ]
