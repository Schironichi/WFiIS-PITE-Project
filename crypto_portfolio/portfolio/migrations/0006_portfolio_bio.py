# Generated by Django 3.2.5 on 2021-12-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20211227_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
