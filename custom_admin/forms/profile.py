from schoolApp.models import Classs, School, Student,Teacher
from django import forms

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher

        exclude=['password','groups','user_permissions','last_login']

    def  clean(self):
        print(self.instance)

    def save(self,commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student

        exclude=['password','groups','user_permissions','last_login']

    def clean(self):
        print(self.instance)

    def save(self,commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance


class SchoolUpdateForm(forms.ModelForm):
    class Meta:
        model = School

        fields = '__all__'

    def  clean(self):
        print(self.instance)

    def save(self,commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance


class ClasssUpdateForm(forms.ModelForm):
    class Meta:
        model = Classs

        fields = '__all__'

    def  clean(self):
        print(self.instance)

    def save(self,commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance