# Generated by Django 2.1.7 on 2020-09-21 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='description',
            new_name='director',
        ),
    ]
