# Generated by Django 4.2.6 on 2023-10-26 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20231024_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ketersediaan',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='vip',
            field=models.TextField(blank=True, null=True),
        ),
    ]
