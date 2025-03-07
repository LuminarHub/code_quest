from django import forms
from .models import *



class StudentForm(forms.ModelForm):
     class Meta:
          model=Student
          fields = ['student_name','email','img','phone','gender','age','password']



class LogForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email","class":"form-control","style":"border-radius: 0.75rem; "}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control","style":"border-radius: 0.75rem; "}))


class StudyNotesForm(forms.ModelForm):
     class Meta:
          model = StudyMaterialNotes
          fields = '__all__'

class StudyFileForm(forms.ModelForm):
     class Meta:
          model = StudyMaterialFile
          fields = '__all__'
