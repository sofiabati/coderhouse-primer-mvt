# Generated by Django 4.1 on 2022-08-05 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_person_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
