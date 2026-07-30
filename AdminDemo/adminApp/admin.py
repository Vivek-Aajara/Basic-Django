from django.contrib import admin

from adminApp.models import student

# Register your models here.



class StudentAdmin(admin.ModelAdmin):
    list_display = ('enrollment','name','age','department')
    search_fields = ('enrollment','name','age','department')
    list_filter = ('enrollment','name','age','department')
    list_per_page = 10



admin.site.register(student, StudentAdmin)