# Generated by Django 3.2.15 on 2022-12-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, verbose_name='phone'),
        ),
    ]
