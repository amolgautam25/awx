# Generated by Django 2.2.16 on 2021-03-26 21:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0135_hostmetrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostmetrics',
            name='first_automation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
