
from django.contrib import admin
from .models import Department, Employee
from import_export.admin import ImportExportModelAdmin
 
 
admin.site.register(Department)
 
 
@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'full_name', 'email', 'designation', 'phone_number', 'salary', 'department', 'is_active', 'manager']
    list_editable = ['salary', 'is_active']
    list_filter = ['salary']
    list_display_links = ['email']
    ordering = ['id']
 
