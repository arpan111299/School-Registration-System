import re
from django.views.generic import FormView
from ..forms import CustomLoginForm


class CustomLoginView(FormView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs