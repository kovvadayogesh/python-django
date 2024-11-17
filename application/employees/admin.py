from django.contrib import admin
from . models import Employee,EmployeeDetails
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name',)
    search_fields = ('employee_name',)

class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('employee_email','employee_phone')
    search_fields = ('employee_email',)


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(EmployeeDetails,EmployeeDetailsAdmin)

