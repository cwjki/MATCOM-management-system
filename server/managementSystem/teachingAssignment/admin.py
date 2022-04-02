from django.contrib import admin
from .models import Career, Department, SchoolYear, Snippet, StudyPlan

admin.site.register(Snippet)
admin.site.register(Career)
admin.site.register(StudyPlan)
admin.site.register(SchoolYear)
admin.site.register(Department)
