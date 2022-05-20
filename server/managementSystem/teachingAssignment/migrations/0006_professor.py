# Generated by Django 4.0.3 on 2022-04-02 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachingAssignment', '0005_classtype_scientificdegree_teachingcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teachingAssignment.department')),
                ('scientificDegree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teachingAssignment.scientificdegree')),
                ('teachingCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teachingAssignment.teachingcategory')),
            ],
        ),
    ]
