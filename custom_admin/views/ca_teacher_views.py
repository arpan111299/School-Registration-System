from django.shortcuts import render , redirect , reverse
from .generic import MyDeleteView, MyListView,MyUpdateView,MyDetailView
from schoolApp.models import Teacher
from ..forms import TeacherUpdateForm

class ProfileListView(MyListView):
    model = Teacher
    template_name = 'customadmin/profile/profile_list.html'
    context_object_name = 'profile'

class ProfileDetailView(MyDetailView):
    model = Teacher
    template_name = 'customadmin/profile/profile_detail.html'
    context_object_name = "profile"

class ProfileUpdateView(MyUpdateView):
    model = Teacher
    form_class = TeacherUpdateForm
    template_name = 'customadmin/profile/profile_update.html'

    def get_success_url(self):
        return reverse('customadmin:profile-list')


class ProfileDeleteView(MyDeleteView):
    model = Teacher
    template_name = 'customadmin/confirm_delete.html'

    def get_success_url(self):
        return reverse('customadmin:profile-list')