# Generated by Django 3.2.15 on 2023-01-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[(None, ''), (1, 'Чоловік'), (2, 'Жінка')], max_length=50, null=True),
        ),
    ]
