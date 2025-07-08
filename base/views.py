from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView


# Create your views here.

class StoreKeeperViLoginRequiredMixin(LoginRequiredMixin):
    login_url = "storekeeper-login-view"


class BaseFormView(FormView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Pass additional data to form constructor
        kwargs['user'] = self.request.user
        return kwargs