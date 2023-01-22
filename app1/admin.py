from django.contrib import admin
from app1.models import Employee, Project

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sal']
admin.site.register(Employee, EmployeeAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Project, ProjectAdmin)