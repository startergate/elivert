# Generated by Django 3.0.7 on 2020-09-18 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20200918_0816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='_password',
            new_name='password',
        ),
    ]