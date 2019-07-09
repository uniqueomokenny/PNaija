# Generated by Django 2.0.5 on 2019-07-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnaija', '0004_feedback_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='title',
            field=models.IntegerField(choices=[(1, 'Enquires'), (2, 'Report Critical Situation'), (3, 'Give Us Your Suggestions')], default=1, max_length=10),
        ),
    ]
