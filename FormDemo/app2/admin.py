from django.contrib import admin
from app2.models import Person2

# Register your models here.
class AdminPerson2(admin.ModelAdmin):
    list_display = ('name','email','age','gender','phone')
    filter = ('gender',)
    search_fields = ('name',)

admin.site.register(Person2,AdminPerson2)