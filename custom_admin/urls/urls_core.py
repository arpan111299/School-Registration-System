from unicodedata import name
from django.urls import path
from . import views

app_name='customadmin'

urlpatterns = [
    path("", views.IndexView.as_view(), name="dashboard"),
        # User
    path("users/", views.UserListView.as_view(), name="user-detail"),

    path("users/<int:pk>/detail/", views.UserDetailView.as_view(), name="user-detailview"),
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("users/create/", views.UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    # path("users/<int:pk>/password/", views.UserPasswordView.as_view(), name="user-password"),
    path("ajax-users", views.UserAjaxPagination.as_view(), name="user-list-ajax"),

    # path("export_user_csv", views.export_user_csv, name="export_user_csv"),
]

urlpatterns += [
    path('posts/',views.PostListView.as_view(),name='post-list'),
    path('posts/create',views.PostCreateView.as_view(),name="post-create"),
    path('posts/<int:pk>/detail/',views.PostDetailView.as_view(),name="post-detailview"),
    path('posts/<int:pk>/delete/',views.PostDeleteView.as_view(),name="post-delete"),
    path('posts/<int:pk>/update/',views.PostUpdateView.as_view(),name="post-update"),
    path('posts/<int:pk>/archive/',views.PostToArchive.as_view(),name="post-archive"),

]

urlpatterns += [
    path('profiles/',views.ProfileListView.as_view(),name="profile-list"),
    path('profiles/<int:pk>/detail/',views.ProfileDetailView.as_view(),name="profile-detailview"),
    path('profiles/<int:pk>/update',views.ProfileUpdateView.as_view(),name="profile-update"),
    path('profiles/<int:pk>/delete',views.ProfileDeleteView.as_view(),name="profile-delete")
]

urlpatterns += [
    path('categories/',views.CategoryListView.as_view(),name='category-list'),
    path('categories/create',views.CategoryCreateView.as_view(),name='category-create'),
    path('categories/<int:pk>/detail/',views.CategoryDetailView.as_view(),name='category-detailview'),
    path('categories/<int:pk>/update',views.CategoryUpdateView.as_view(),name='category-update'),
    path('categories/<int:pk>/delete',views.CategoryDeleteView.as_view(),name='category-delete')
]

urlpatterns += [
    path('comments/',views.CommentListView.as_view(),name='comment-list'),
    path('comments/create',views.CommentCreateView.as_view(),name='comment-create'),
    path('comments/<int:pk>/detail/',views.CommentDetailView.as_view(),name='comment-detailview'),
    path('comments/<int:pk>/update',views.CommentUpdateView.as_view(),name='comment-update'),
    path('comments/<int:pk>/delete',views.CommentDeleteView.as_view(),name='comment-delete'),
]
    