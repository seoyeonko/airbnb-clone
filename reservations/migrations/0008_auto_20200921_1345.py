# Generated by Django 2.2.5 on 2020-09-21 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_auto_20200921_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('canceled', 'Canceled'), ('pending', 'Pending')], default='pending', max_length=12),
        ),
    ]
