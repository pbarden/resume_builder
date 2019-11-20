from django.contrib import admin
from .models import UserProfile, Job, Skill, Degree, Project

admin.site.register(UserProfile)
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Degree)
admin.site.register(Project)