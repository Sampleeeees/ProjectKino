# Generated by Django 3.2.15 on 2023-01-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0037_auto_20230125_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[(None, ''), ('1', 'Українська'), ('2', 'Англійська')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[(None, ''), ('2', 'Жінка'), ('1', 'Чоловік')], max_length=50, null=True),
        ),
    ]