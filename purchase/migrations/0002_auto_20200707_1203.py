# Generated by Django 3.0.7 on 2020-07-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processed', 'Processed'), ('canceled', 'Canceled'), ('failed', 'Failed')], default='pending', max_length=16),
        ),
    ]
