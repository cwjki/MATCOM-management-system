# Generated by Django 4.0.3 on 2022-08-06 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachingAssignment', '0024_teachingassignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teachingAssignment.career')),
            ],
        ),
    ]
