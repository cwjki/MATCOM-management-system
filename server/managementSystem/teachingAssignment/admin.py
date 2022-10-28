from django.contrib import admin
from .models import Career, ClassType, Department, Professor, TeachingAssignment, TeachingGroup, ScientificDegree, StudyPlan, Subject, TeachingCategory, TeachingPlanning, TimePeriod, Semester, CarmenTable, SubjectDescription, Faculty


admin.site.register(Career)
admin.site.register(StudyPlan)
admin.site.register(TeachingGroup)
admin.site.register(Semester)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(ScientificDegree)
admin.site.register(TeachingCategory)
admin.site.register(TimePeriod)
admin.site.register(ClassType)
admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(CarmenTable)
admin.site.register(SubjectDescription)
admin.site.register(TeachingAssignment)
admin.site.register(TeachingPlanning)
