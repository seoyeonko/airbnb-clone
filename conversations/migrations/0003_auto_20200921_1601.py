# Generated by Django 2.2.5 on 2020-09-21 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20200921_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='conversations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='conversations.Conversation'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
