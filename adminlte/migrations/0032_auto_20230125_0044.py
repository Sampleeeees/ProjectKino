# Generated by Django 3.2.15 on 2023-01-25 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0031_alter_speedcarousel_speed_carousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='type_2d',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='session',
            name='type_3d',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='session',
            name='type_imax',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='speedcarousel',
            name='speed_carousel',
            field=models.CharField(blank=True, choices=[(None, ''), ('7000', '7c'), ('10000', '10c'), ('3000', '3c'), ('5000', '5c')], max_length=50, null=True),
        ),
    ]
