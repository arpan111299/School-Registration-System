from dataclasses import field
from distutils.command.clean import clean
import email
from schoolApp.models import Student
from django import forms


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'username',
            'is_student',
            'has_school',
            'age',
            'access_token'
        ]

    def __init__(self,*args,**kwargs):
        return super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(StudentCreationForm,self).clean()
        # print(cleaned_data)
        first_name = cleaned_data.get('first_name')    
        last_name = cleaned_data.get('last_name')    
        email = cleaned_data.get('category')
        phone = cleaned_data.get('phone')
        username = cleaned_data.get('username')
        is_student = cleaned_data.get('is_student')
        has_school = cleaned_data.get('has_school')
        age = cleaned_data.get('age')
        access_token = cleaned_data.get('access_token')

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['is_staff','is_active']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(PostUpdateForm,self).clean()
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance
    
# class PostToArchiveForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['soft_delete']
    
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
    
#     def clean(self):
#         cleaned_data = super(PostToArchiveForm,self).clean()
#         print(cleaned_data)
    
#     def save(self, commit=True):
#         instance = super().save(commit=False)

#         if commit:
#             instance.save()
#         return instance