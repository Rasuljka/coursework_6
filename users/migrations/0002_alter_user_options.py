# Generated by Django 4.2.7 on 2024-06-29 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_user_deactivate', 'Can deactivate user')], 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]