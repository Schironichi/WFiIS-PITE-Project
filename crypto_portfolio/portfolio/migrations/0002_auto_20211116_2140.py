# Generated by Django 3.2.5 on 2021-11-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
