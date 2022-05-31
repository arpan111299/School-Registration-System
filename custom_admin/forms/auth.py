from schoolApp.models import Teacher
from django.contrib import auth
from django import forms
from django.contrib.auth.hashers import check_password

class CustomLoginForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'email',
            'password'
        ]

    def __init__(self,request=None,*args,**kwargs):
            self.request = request
            print(kwargs)
            print(kwargs.get('request'))
            self.user_cache = None
            super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(CustomLoginForm,self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if Teacher.objects.filter(email=email).exists():
            if email is not None and password:
                
                self.user_cache=auth.authenticate(self.request,email=email,password=password)
                print(self.user_cache)
                user = Teacher.objects.get(email=email)
                print(user)
                print(check_password(user.password,password))
                if check_password(user.password,password):
                    print("password Checked")
                    auth.login(self.request,user)
                else:
                    print("password not checked")
    