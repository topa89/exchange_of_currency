# Generated by Django 2.0.2 on 2018-02-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180211_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='limit_val',
            name='min_val',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4),
        ),
    ]
