from django.contrib import admin
from .models import Career, ClassType, Department, Professor, SchoolYear, ScientificDegree, Snippet, StudyPlan, TeachingCategory, YearPeriod

admin.site.register(Snippet)
admin.site.register(Career)
admin.site.register(StudyPlan)
admin.site.register(SchoolYear)
admin.site.register(Department)
admin.site.register(ScientificDegree)
admin.site.register(TeachingCategory)
admin.site.register(YearPeriod)
admin.site.register(ClassType)
admin.site.register(Professor)
