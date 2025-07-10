from django.contrib.auth import login, get_user_model
from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.urls import reverse_lazy, reverse
from django.views import View
from django_tables2 import SingleTableView

from base.variables import PAGINATED_BY_VALUE
from base.views import StoreKeeperViLoginRequiredMixin
from user.forms import StorekeeperLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

from user.models import Customer
from user.tables import UserTable, CustomerTable


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


class UserListView(StoreKeeperViLoginRequiredMixin ,SingleTableView, ListView):
    model = get_user_model()
    table_class = UserTable
    template_name = "dashboard/tables.html"
    paginate_by = PAGINATED_BY_VALUE

    def get_queryset(self):
        return get_user_model().objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creation_link"] = {
            "title": "ایجاد کاربر جدید",
            "link": reverse("product-create-view")
        }
        context["title"] = "لیست کاربران"
        return context


class CustomerListView(StoreKeeperViLoginRequiredMixin ,SingleTableView, ListView):
    model = Customer
    table_class = CustomerTable
    template_name = "dashboard/tables.html"
    paginate_by = PAGINATED_BY_VALUE

    def get_queryset(self):
        return Customer.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creation_link"] = {
            "title": "ایجاد مشتری جدید",
            "link": reverse("product-create-view")
        }
        context["title"] = "لیست مشتریان"
        return context
