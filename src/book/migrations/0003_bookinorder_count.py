# Generated by Django 4.0.6 on 2022-07-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_order_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinorder',
            name='count',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
