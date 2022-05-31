from django import forms
from django.forms import ModelForm
from .models import *

class AddSchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['school_name','address','school_phone']


class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','email']


class AddClassForm(ModelForm):
    class Meta:
        model = Classs
        fields = ['standard','division','access_code']


class TeacherUpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','email','access_token']