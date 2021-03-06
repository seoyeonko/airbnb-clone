# Generated by Django 2.2.5 on 2020-09-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_auto_20200921_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('canceled', 'Canceled')], default='pending', max_length=12),
        ),
    ]
