# Generated by Django 3.2.15 on 2023-01-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0014_alter_speedcarousel_speed_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedcarousel',
            name='speed_carousel',
            field=models.CharField(blank=True, choices=[(700, '7c'), (1000, '10c'), (500, '5c'), (300, '3c')], max_length=50, null=True),
        ),
    ]
