# Generated by Django 3.2.15 on 2023-01-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedcarousel',
            name='speed_carousel',
            field=models.CharField(blank=True, choices=[('4', '8c'), ('5', '9c'), ('2', '6c'), ('3', '7c'), ('1', '5c'), ('6', '10c')], max_length=50, null=True),
        ),
    ]
