# Generated by Django 4.0.3 on 2022-08-08 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachingAssignment', '0034_teachingplanning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='created',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='updated',
        ),
    ]