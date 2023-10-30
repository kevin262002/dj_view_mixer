from django.forms import fields  
from .models import Employee  
from django import forms  
  
class EmployeeForm(forms.Form):
    class Meta:
        model = Employee  
        fields = '__all__'  