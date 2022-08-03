# Generated by Django 4.0.3 on 2022-08-03 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachingAssignment', '0016_remove_subjectdescription_string_repr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cotutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotutor', to='teachingAssignment.professor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachingAssignment.student')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to='teachingAssignment.professor')),
            ],
        ),
        migrations.CreateModel(
            name='ThesisCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to='teachingAssignment.professor')),
                ('secretary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secretary', to='teachingAssignment.professor')),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachingAssignment.thesis')),
            ],
        ),
    ]
