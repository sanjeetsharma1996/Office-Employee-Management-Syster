from django import forms
from .models import Department,Role,Employee

class departmentFrorm(forms.ModelForm):
 class Meta:
  model = Department 
  fields = ['D_Name','D_location']

class roleForm(forms.ModelForm):
 class Meta:
  model = Role 
  fields = ['R_Name']

class employeeForm(forms.ModelForm):
 class Meta:
  model = Employee
  fields = '__all__'

  labels = {'First_Name':'First Name', 
            'Last_Name':'Last Name', 
            'Email':'Email ID',
            'Salary': 'Salary',
            'Bonus': 'Bonus',
            'D_Name':'Department Name',
            'D_location':'Department location',
            'R_Name': 'Role',
            'Phone':'Phone Number',
            'Hire_date': 'Hire Date'
            }

  widgets = {
          'First_Name':forms.TextInput(attrs={'class':'form-control'}),
          'Last_Name':forms.TextInput(attrs={'class':'form-control'}),
          'Email':forms.EmailInput(attrs={'class':'form-control'}),
          'Salary':forms.NumberInput(attrs={'class':'form-control'}),
          'Bonus':forms.NumberInput(attrs={'class':'form-control'}),
          'D_Name':forms.TextInput(attrs={'class':'form-control'}),
          'D_location':forms.TextInput(attrs={'class':'form-control'}),
          'R_Name':forms.TextInput(attrs={'class':'form-control'}),
          'Phone':forms.NumberInput(attrs={'class':'form-control'}),
          'Hire_date':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),

           }
