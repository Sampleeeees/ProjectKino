# Generated by Django 3.2.15 on 2023-01-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20230114_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[(1, 'Українська'), (2, 'Англійська')], max_length=50, null=True),
        ),
    ]
