# Generated by Django 5.1.7 on 2025-03-08 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcheck', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='user',
            new_name='userMail',
        ),
    ]
