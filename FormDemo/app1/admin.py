from django.contrib import admin
from app1 import models
from app1.models import Person


# Register your models here.

class AdminPerson(admin.ModelAdmin):
    list_display = ('name','email','phone','gender')
    list_filter = ('name','email','phone','gender')
    search_fields = ('name',)

admin.site.register(Person,AdminPerson)