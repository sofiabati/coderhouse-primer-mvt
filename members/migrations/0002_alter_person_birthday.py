# Generated by Django 4.1 on 2022-08-05 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.CharField(max_length=15),
        ),
    ]