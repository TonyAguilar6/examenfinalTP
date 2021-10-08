# Generated by Django 2.0.6 on 2021-10-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webprogra', '0002_auto_20211006_2018'),
    ]

    operations = [
        migrations.DeleteModel(
            name='lap',
        ),
        migrations.AddField(
            model_name='employee',
            name='marca',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='modelo',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='ram',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='rom',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
