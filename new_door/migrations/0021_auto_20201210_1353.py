# Generated by Django 3.1.4 on 2020-12-10 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0020_auto_20201210_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/profile_pic'),
        ),
    ]
