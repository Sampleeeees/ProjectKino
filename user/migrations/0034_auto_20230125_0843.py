# Generated by Django 3.2.15 on 2023-01-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_auto_20230125_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('1', 'Українська'), ('2', 'Англійська'), (None, '')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('1', 'Чоловік'), ('2', 'Жінка'), (None, '')], max_length=50, null=True),
        ),
    ]
