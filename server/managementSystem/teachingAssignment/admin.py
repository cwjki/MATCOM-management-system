from django.contrib import admin
from .models import Department, Career, Professor, ClassType, SchoolYear, ScientificDegree, StudyPlan, Subject, TeachingAssigment, TeachingCategory, TeachingPlanning, YearPeriod

admin.site.register(Department)
admin.site.register(Career)
admin.site.register(ClassType)
admin.site.register(SchoolYear)
admin.site.register(ScientificDegree)
admin.site.register(TeachingCategory)
admin.site.register(YearPeriod)
admin.site.register(StudyPlan)

admin.site.register(Subject)
admin.site.register(Professor)

admin.site.register(TeachingPlanning)
admin.site.register(TeachingAssigment)
