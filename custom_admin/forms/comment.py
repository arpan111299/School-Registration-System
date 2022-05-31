from dataclasses import field
from django import forms
from ..models import Comment

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment',
            'user',
            'post'
        ]
    
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        return super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(CommentCreateForm,self).clean()
        # print(cleaned_data)
        title = cleaned_data.get('name')


    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance