from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.views import View

from base.views import StoreKeeperViLoginRequiredMixin
from user.forms import StorekeeperLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class StorekeeperLoginView(FormView):
    template_name = "users/storekeeper_login.html"
    form_class = StorekeeperLoginForm
    success_url = reverse_lazy("dashboard-view")

    def form_valid(self, form):
        login(self.request, form.storekeeper)
        return super().form_valid(form)


class DashboardView(StoreKeeperViLoginRequiredMixin, View):
    def get(self, request):
        context = {
            "title": "داشبورد"
        }
        return render(request, "dashboard/main.html", context)