# Generated by Django 3.2.15 on 2023-01-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0042_auto_20230127_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='template',
            field=models.FileField(blank=True, upload_to='file/mailing/'),
        ),
        migrations.AlterField(
            model_name='speedcarousel',
            name='speed_carousel',
            field=models.CharField(blank=True, choices=[('7000', '7c'), (None, ''), ('5000', '5c'), ('3000', '3c'), ('10000', '10c')], max_length=50, null=True),
        ),
    ]
