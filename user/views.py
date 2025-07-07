from django.contrib.auth import login
from django.views.generic import FormView
from django.urls import reverse_lazy

from user.forms import StorekeeperLoginForm


# Create your views here.


class StorekeeperLoginView(FormView):
    template_name = "users/storekeeper_login.html"
    form_class = StorekeeperLoginForm
    success_url = reverse_lazy("warehouse:dashboard")

    def form_valid(self, form):
        login(self.request, form.storekeeper)
        return super().form_valid(form)