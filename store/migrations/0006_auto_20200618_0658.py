# Generated by Django 3.0.6 on 2020-06-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200618_0658'),
        ('store', '0005_auto_20200615_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='registerer',
            field=models.ManyToManyField(to='account.User'),
        ),
    ]
