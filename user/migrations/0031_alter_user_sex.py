# Generated by Django 3.2.15 on 2023-01-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_auto_20230125_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('1', 'Чоловік'), (None, ''), ('2', 'Жінка')], max_length=50, null=True),
        ),
    ]