from django.urls import path
from school_api.views.teachers_views import *
from school_api.views.student_views import *
from school_api.views.school_views import *
from school_api.views.class_views import *


urlpatterns = [
    # Teacher API
    path('teacherapi/', TeacherAPI.as_view()),
    path('teacherapi/<int:id>', TeacherAPI.as_view()),

    #Student API
    path('studentapi/', StudentAPI.as_view()),
    path('studentapi/<int:id>', StudentAPI.as_view()),

    #School API
    path('schoolapi/', SchoolAPI.as_view()),
    path('schoolapi/<int:id>', SchoolAPI.as_view()),

    #Class API
    path('classapi/', ClasssAPI.as_view()),
    path('classapi/<int:id>', ClasssAPI.as_view()),
]