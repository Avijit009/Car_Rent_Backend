# Generated by Django 4.1.7 on 2024-02-24 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_car_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_image',
        ),
    ]