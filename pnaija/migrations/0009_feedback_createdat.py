# Generated by Django 2.0.5 on 2019-07-08 08:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pnaija', '0008_auto_20190708_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
