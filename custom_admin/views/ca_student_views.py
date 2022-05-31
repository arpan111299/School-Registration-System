from django.shortcuts import render , redirect , reverse
from .generic import MyDeleteView, MyListView,MyUpdateView,MyDetailView
from schoolApp.models import Student
from ..forms import StudentUpdateForm

class ProfileListView(MyListView):
    model = Student
    template_name = 'customadmin/profile/profile_list.html'
    context_object_name = 'profile'

class ProfileDetailView(MyDetailView):
    model = Student
    template_name = 'customadmin/profile/profile_detail.html'
    context_object_name = "profile"

class ProfileUpdateView(MyUpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'customadmin/profile/profile_update.html'

    def get_success_url(self):
        return reverse('customadmin:profile-list')


class ProfileDeleteView(MyDeleteView):
    model = Student
    template_name = 'customadmin/confirm_delete.html'

    def get_success_url(self):
        return reverse('customadmin:profile-list')