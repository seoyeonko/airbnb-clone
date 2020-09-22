# Generated by Django 2.2.5 on 2020-09-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20200915_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('canceled', 'Canceled'), ('pending', 'Pending'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]