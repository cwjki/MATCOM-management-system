from django.contrib import admin
from .models import Career, ClassType, Department, Professor, SchoolYear, ScientificDegree, Snippet, StudyPlan, Subject, TeachingAssignment, TeachingCategory, TeachingPlanning, YearPeriod, Semester, CarmenTable

admin.site.register(Career)
admin.site.register(StudyPlan)
admin.site.register(SchoolYear)
admin.site.register(Semester)
admin.site.register(Department)
admin.site.register(ScientificDegree)
admin.site.register(TeachingCategory)
admin.site.register(YearPeriod)
admin.site.register(ClassType)
admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(CarmenTable)
admin.site.register(TeachingPlanning)
admin.site.register(TeachingAssignment)
