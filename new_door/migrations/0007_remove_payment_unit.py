# Generated by Django 3.1.4 on 2021-02-06 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0006_payment_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='unit',
        ),
    ]
