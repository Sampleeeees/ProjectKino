# Generated by Django 3.2.15 on 2023-01-14 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_user_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[(None, ''), (1, 'Українська'), (2, 'Англійська')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[(1, 'Чоловік'), (None, ''), (2, 'Жінка')], max_length=50, null=True),
        ),
    ]
