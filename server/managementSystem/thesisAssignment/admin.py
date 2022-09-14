from django.contrib import admin
from .models import Student, Thesis, ThesisCommittee

# Register your models here.
admin.site.register(Student)
admin.site.register(Thesis)
admin.site.register(ThesisCommittee)
