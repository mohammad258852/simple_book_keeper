# Generated by Django 4.0.6 on 2022-07-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_bookinorder_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
