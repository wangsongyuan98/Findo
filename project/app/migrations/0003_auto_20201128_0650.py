# Generated by Django 3.0.5 on 2020-11-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userclicks_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userclicks',
            name='stock_id',
        ),
        migrations.AddField(
            model_name='userclicks',
            name='company',
            field=models.CharField(default='unknown', max_length=255),
        ),
    ]
