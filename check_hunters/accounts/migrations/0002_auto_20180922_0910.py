# Generated by Django 2.0.8 on 2018-09-22 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='check',
            name='from_account',
        ),
        migrations.RemoveField(
            model_name='check',
            name='to_client',
        ),
        migrations.DeleteModel(
            name='Check',
        ),
    ]