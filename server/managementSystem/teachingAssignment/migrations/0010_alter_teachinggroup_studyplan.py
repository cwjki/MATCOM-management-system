# Generated by Django 4.0.3 on 2022-04-14 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachingAssignment', '0009_rename_teachingplanning_subjectdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachinggroup',
            name='studyPlan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teachingGroups', to='teachingAssignment.studyplan'),
        ),
    ]