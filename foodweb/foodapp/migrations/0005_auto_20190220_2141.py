# Generated by Django 2.1.4 on 2019-02-20 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_auto_20190217_0258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manu',
            new_name='Menu',
        ),
    ]