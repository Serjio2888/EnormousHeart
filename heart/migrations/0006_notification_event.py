# Generated by Django 2.1.7 on 2019-03-30 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0005_auto_20190330_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='heart.Event'),
            preserve_default=False,
        ),
    ]
