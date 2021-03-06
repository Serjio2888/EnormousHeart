# Generated by Django 2.1.7 on 2019-03-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0004_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volonteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя волонтера')),
                ('pass_hash', models.CharField(max_length=255, verbose_name='хэш пароля')),
                ('info', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.RemoveField(
            model_name='notification',
            name='event',
        ),
        migrations.AddField(
            model_name='notification',
            name='author',
            field=models.CharField(default='Волонтер', max_length=80, verbose_name='Ваше имя'),
            preserve_default=False,
        ),
    ]
