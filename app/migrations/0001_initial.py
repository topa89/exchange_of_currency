# Generated by Django 2.0.2 on 2018-02-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='limit_val',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('reserve', models.IntegerField(default=0)),
            ],
        ),
    ]
