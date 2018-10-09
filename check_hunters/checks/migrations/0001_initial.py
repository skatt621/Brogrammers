# Generated by Django 2.0.8 on 2018-09-22 18:32

import checks.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20180922_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, validators=[checks.models.validate_positive])),
                ('made_date', models.DateField()),
                ('check_num', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('paid_date', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('from_account', models.ForeignKey(help_text='routing#:account#', on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('to_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Client')),
            ],
        ),
    ]