# Generated by Django 3.2.15 on 2022-12-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20221227_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
