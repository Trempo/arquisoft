# Generated by Django 3.2.6 on 2021-10-13 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comercios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('comercio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='comercios.comercio')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
