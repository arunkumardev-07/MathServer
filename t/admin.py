from django.contrib import admin
from myapp.models import Employee  # Ensure 'myapp' is correct

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')  # Columns to display in Django Admin
    search_fields = ('name', 'position')  # Enable search functionality






