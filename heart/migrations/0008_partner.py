# Generated by Django 2.1.7 on 2019-03-30 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0007_remove_notification_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя компании')),
                ('role', models.TextField(blank=True, verbose_name='Что делает для мероприятия?')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heart.Event')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heart.Task')),
            ],
        ),
    ]