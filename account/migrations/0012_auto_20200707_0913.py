# Generated by Django 3.0.7 on 2020-07-07 09:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200618_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]