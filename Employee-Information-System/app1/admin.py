from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list=['name','email','password']
# Register your models here.
admin.site.register(Employee,EmployeeAdmin)

