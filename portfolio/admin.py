from django.contrib import admin

# Register your models here.
from portfolio.models import Project, Stack, Сertificate

admin.site.register(Project)
admin.site.register(Stack)
admin.site.register(Сertificate)