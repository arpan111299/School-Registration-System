from django.urls import path
from schoolApp.views.classes_views import *
from schoolApp.views.schools_views import *
from schoolApp.views.students_views import *
from schoolApp.views.teachers_views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
#Teacher's URL
    path('', IndexView.as_view(), name="Index"),
    path('teachersignup/',TeacherSignUpView.as_view(), name="TeacherSignUp"),
    path('teacherlogin/',TeacherLogInView.as_view(), name='TeacherLogIn'),
    path('teacher_mainbody/',(TeacherMainBodyView.as_view()), name="TeacherMainBody"),
    path('teacher_school_detail/<int:id>',TeacherSchoolDetailedView.as_view(), name="TeacherDetailed"),
    path('teacher_logout/', TeacherLogout.as_view(), name="TeacherLogout"),
    path('teacher_class_update/<id>',login_required(TeacherClassUpdateView.as_view()),name="TeacherClassUpdate"),
    path('teacher_student_update/<pk>',login_required(TeacherUpdateStudentView.as_view()),name="TeacherUpdateStudent"),
    path('admin_teacher_remove/<str:username>',login_required(AdminRemoveTeacherView.as_view()),name="AdminRemoveTeacher"),
    path('teacher_to_existing_school/<int:id>',login_required(TeacherAddToExistingSchoolView.as_view()),name="TeacherAddToExistingSchool"),
    path('teacher_to_existing_class/<int:access_code>',login_required(TeacherAddToExistingClassView.as_view()),name="TeacherAddToExistingClass"),


#Student's URL
    path('studentsignup/',StudentSignUpView.as_view(), name="StudentSignUp"),
    path('student_login/',StudentLogInView.as_view(), name='StudentLogIn'),
    path('student_mainbody/<int:id>',login_required(StudentMainBodyView.as_view()), name="StudentMainBody"),
    path('student_logout/', login_required(StudentLogout.as_view()), name="StudentLogout"),
    path('student_acces_code_search/',login_required(StudentAccessCodeSearchView.as_view()), name="StudentAccessCodeSearch"),
    path('student_update/<int:id>',login_required(StudentUpdateView.as_view()),name="StudentUpdate"),


#School's URL
    path('school_create/',CreateSchoolView.as_view(),name='TeacherSchoolCreate'),


#Class' URL
    path('class_create/',TeacherClassCreateView.as_view(),name='TeacherClassCreate'),
]
