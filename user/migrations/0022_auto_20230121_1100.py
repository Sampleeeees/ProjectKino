# Generated by Django 3.2.15 on 2023-01-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20230120_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('1', 'Українська'), (None, ''), ('2', 'Англійська')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('1', 'Чоловік'), (None, ''), ('2', 'Жінка')], max_length=50, null=True),
        ),
    ]
