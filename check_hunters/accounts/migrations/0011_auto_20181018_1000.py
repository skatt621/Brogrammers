# Generated by Django 2.1.2 on 2018-10-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20181011_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
