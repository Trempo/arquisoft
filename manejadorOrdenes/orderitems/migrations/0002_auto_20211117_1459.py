# Generated by Django 2.1.3 on 2021-11-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderitems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
