# Generated by Django 2.1.7 on 2019-03-30 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0006_notification_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='event',
        ),
    ]
