# Generated by Django 4.0.3 on 2022-05-15 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0002_alter_coursemodel_assigned_instructor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
