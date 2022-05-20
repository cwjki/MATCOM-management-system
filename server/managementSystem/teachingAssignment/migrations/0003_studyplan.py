# Generated by Django 4.0.3 on 2022-04-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachingAssignment', '0002_career_delete_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('since', models.DateField()),
                ('until', models.DateField(blank=True, null=True)),
                ('numberOfSemesters', models.SmallIntegerField()),
            ],
        ),
    ]
