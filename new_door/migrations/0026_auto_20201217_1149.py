# Generated by Django 3.1.4 on 2020-12-17 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0025_auto_20201217_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenantcontract',
            name='unit',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='new_door.unit'),
        ),
    ]
