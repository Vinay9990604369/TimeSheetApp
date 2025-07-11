from django.contrib import admin
from .models import TimeSheetEntry, UserProfile

admin.site.register(TimeSheetEntry)
admin.site.register(UserProfile)
