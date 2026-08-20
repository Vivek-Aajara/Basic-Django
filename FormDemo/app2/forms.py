from django import forms
from .models import Person2

class Person2Form(forms.ModelForm):
    class Meta:
        model = Person2
        fields = ['name','email','age','gender','phone']
