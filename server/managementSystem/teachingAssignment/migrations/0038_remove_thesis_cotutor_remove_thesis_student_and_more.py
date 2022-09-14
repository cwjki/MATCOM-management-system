# Generated by Django 4.0.3 on 2022-09-14 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachingAssignment', '0037_delete_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='cotutor',
        ),
        migrations.RemoveField(
            model_name='thesis',
            name='student',
        ),
        migrations.RemoveField(
            model_name='thesis',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='thesiscommittee',
            name='opponent',
        ),
        migrations.RemoveField(
            model_name='thesiscommittee',
            name='secretary',
        ),
        migrations.RemoveField(
            model_name='thesiscommittee',
            name='thesis',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Thesis',
        ),
        migrations.DeleteModel(
            name='ThesisCommittee',
        ),
    ]