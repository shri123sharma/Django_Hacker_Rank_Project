# Generated by Django 4.2.5 on 2023-09-18 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing_model_app', '0002_mymodel_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='number',
        ),
    ]
