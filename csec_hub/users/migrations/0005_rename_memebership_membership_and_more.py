# Generated by Django 4.0.4 on 2022-05-07 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('users', '0004_alter_user_profile_picture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Memebership',
            new_name='Membership',
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'verbose_name': 'Membership'},
        ),
    ]
