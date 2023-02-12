# Generated by Django 3.2.15 on 2023-01-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20230121_1100'),
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
            field=models.CharField(blank=True, choices=[('1', 'Чоловік'), ('2', 'Жінка'), (None, '')], max_length=50, null=True),
        ),
    ]