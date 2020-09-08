# Generated by Django 3.0.7 on 2020-09-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0017_auto_20200907_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partialorder',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('ready', 'Ready'), ('delivering', 'Delivering'), ('delivered', 'Delivered'), ('canceled', 'Canceled')], default='pending', max_length=16),
        ),
    ]