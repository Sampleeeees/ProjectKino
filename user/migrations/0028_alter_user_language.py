# Generated by Django 3.2.15 on 2023-01-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_auto_20230125_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[(None, ''), ('2', 'Англійська'), ('1', 'Українська')], max_length=50, null=True),
        ),
    ]
