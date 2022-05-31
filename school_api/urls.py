from django.urls import path
from school_api.views.teachers_views import *
from school_api.views.student_views import *
from school_api.views.school_views import *
from school_api.views.class_views import *
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView
# from drf_yasg import openapi
# from django.views.generic import TemplateView
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view


# schema_view = get_schema_view(
#     openapi.Info(
#         title='CRUD API',
#         default_version="v1",
#         description='Test 1'
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )




urlpatterns = [
    # Teacher API
    path('teacher/list/', TeacherListAPI.as_view()),
    path('teacher/<int:pk>/', TeacherAPI.as_view()),
    path('admin-remove-teacher/<pk>',AdminRemoveTeacherAPI.as_view()),

    #Student API
    path('student/list/', StudentListAPI.as_view()),
    path('student/<int:pk>/', StudentAPI.as_view()),

    #School API
    path('school/list/', SchoolListAPI.as_view()),
    path('school/<int:pk>/', SchoolAPI.as_view()),

    #Class API
    path('class/list/', ClasssListAPI.as_view()),
    path('class/<int:pk>/', ClasssAPI.as_view()),

    #Token Authnetication API
    # path('get-token/simple-token/auth/', obtain_auth_token),

    #JWT Token Authentication API
    path('get-token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh-token/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='token_verify'),

    #User LogOut using Token BlackList
    path('auth/user/logout/',UserLogout.as_view(),name='UserLogOut'),
]


# urlpatterns += [
#     # ...
#     # Route TemplateView to serve Swagger UI template.
#     #   * Provide `extra_context` with view name of `SchemaView`.
#     path('swagger-ui/', TemplateView.as_view(
#         template_name='swagger_ui.html',
#         extra_context={'schema_url':'openapi-schema'}
#     ), name='api_doc'),
# ]


# urlpatterns += [
#     path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='openapi-schema')
# ]