# Generated by Django 5.1.7 on 2025-03-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcheck', '0004_userlog_userlogout_userlog_userlogoutt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latOffice', models.CharField(default='NIL', max_length=30)),
                ('longOffice', models.CharField(default='NIL', max_length=30)),
                ('radOffice', models.CharField(default='NIL', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='userAtt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attDate', models.CharField(default='NIL', max_length=25)),
                ('att', models.CharField(default='NIL', max_length=25)),
            ],
        ),
    ]
