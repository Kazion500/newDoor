# Generated by Django 3.1.4 on 2020-12-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0013_auto_20201209_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenantcontract',
            name='annual_rent',
            field=models.PositiveIntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tenantcontract',
            name='discount',
            field=models.PositiveIntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tenantcontract',
            name='end_date',
            field=models.DateField(max_length=50),
        ),
    ]
