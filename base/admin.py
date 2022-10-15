from django.contrib import admin
from .models import Company, SocialAccount, Advocate, Project, Skill, Tech

admin.site.register(Company)
admin.site.register(SocialAccount)
admin.site.register(Advocate)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tech)