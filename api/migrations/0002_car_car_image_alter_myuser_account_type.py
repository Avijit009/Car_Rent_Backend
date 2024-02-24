# Generated by Django 4.1.7 on 2024-02-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(default='', upload_to='car_photos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='account_type',
            field=models.CharField(default='client', help_text='Car Owner can use their car(s) for rentin and Clients can rent those car.', max_length=64),
        ),
    ]