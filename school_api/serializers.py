from schoolApp.models import *
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        exclude=['password','groups','user_permissions','last_login']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        exclude=['password','groups','user_permissions','last_login']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields= "__all__"

class ClasssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classs
        fields="__all__"