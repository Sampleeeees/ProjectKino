# Generated by Django 3.2.15 on 2023-01-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_user_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[(1, 'Англійська'), (None, 'Українська')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[(1, 'Жінка'), (None, 'Чоловік')], max_length=50, null=True),
        ),
    ]
