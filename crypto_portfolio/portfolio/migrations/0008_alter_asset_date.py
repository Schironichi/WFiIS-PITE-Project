# Generated by Django 3.2.5 on 2022-01-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_remove_portfolio_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
