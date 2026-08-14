from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("roll_no", "name", "email", "course", "year", "phone")
    search_fields = ("roll_no", "name", "email")
    list_filter = ("course", "year")
