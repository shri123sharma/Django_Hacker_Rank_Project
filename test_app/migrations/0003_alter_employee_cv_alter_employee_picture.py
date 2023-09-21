# Generated by Django 4.2.4 on 2023-08-21 13:46

from django.db import migrations, models
import test_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_employee_slug_alter_employee_cv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='cv',
            field=models.FileField(upload_to=test_app.models.employee_picture_path),
        ),
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(upload_to=test_app.models.employee_picture_path),
        ),
    ]
