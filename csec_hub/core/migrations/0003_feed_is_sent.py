# Generated by Django 4.0.4 on 2022-05-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_subscription_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
    ]
