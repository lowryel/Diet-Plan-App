# Generated by Django 4.0 on 2022-02-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_planapp', '0005_auto_20211211_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='fill_formmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
