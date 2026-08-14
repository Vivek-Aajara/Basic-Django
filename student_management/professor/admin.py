from django.contrib import admin
from .models import Professor, Subject


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("emp_id", "name", "email", "department", "phone")
    search_fields = ("emp_id", "name", "email")
    list_filter = ("department",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "credits", "professor")
    search_fields = ("code", "name")
    list_filter = ("professor",)
