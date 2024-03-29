# Generated by Django 4.0.3 on 2022-08-04 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachingAssignment', '0019_delete_carmentable'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarmenTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachingAssignment.semester')),
                ('study_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachingAssignment.studyplan')),
                ('teaching_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachingAssignment.teachinggroup')),
                ('time_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachingAssignment.timeperiod')),
            ],
        ),
    ]
