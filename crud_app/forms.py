from django import forms
from crud_app.models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at']