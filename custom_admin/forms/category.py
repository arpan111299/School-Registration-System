from django import forms
from schoolApp.models import School

class SchoolCreationForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        return super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(SchoolCreationForm,self).clean()
        # print(cleaned_data)
        title = cleaned_data.get('name')


    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance

class SchoolUpdateForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(SchoolUpdateForm,self).clean()
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance