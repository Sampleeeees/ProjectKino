# Generated by Django 3.2.15 on 2023-02-11 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0048_auto_20230211_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('2', 'Англійська'), (None, ''), ('1', 'Українська')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('1', 'Чоловік'), (None, ''), ('2', 'Жінка')], max_length=50, null=True),
        ),
    ]
