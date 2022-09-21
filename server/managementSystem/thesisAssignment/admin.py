from django.contrib import admin
from .models import Place, Keyword, Thesis, ThesisCommittee

# Register your models here.
admin.site.register(Place)
admin.site.register(Keyword)
admin.site.register(Thesis)
admin.site.register(ThesisCommittee)
