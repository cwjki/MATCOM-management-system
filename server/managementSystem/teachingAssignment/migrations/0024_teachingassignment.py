# Generated by Django 4.0.3 on 2022-08-05 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachingAssignment', '0023_subjectdescription_delete_teachingassignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(default=1)),
                ('group', models.IntegerField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachingAssignment.professor')),
                ('subject_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachingAssignment.subjectdescription')),
            ],
        ),
    ]