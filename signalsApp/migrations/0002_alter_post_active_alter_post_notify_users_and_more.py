# Generated by Django 4.1.1 on 2022-09-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signalsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='notify_users',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='notify_users_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
