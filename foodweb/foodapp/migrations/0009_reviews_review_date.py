# Generated by Django 2.1.4 on 2019-02-24 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0008_auto_20190221_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='review_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
