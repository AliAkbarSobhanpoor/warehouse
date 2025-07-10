from django.shortcuts import render, reverse
from django.views.generic import ListView
from django_tables2 import SingleTableView

from base.variables import PAGINATED_BY_VALUE
from base.views import StoreKeeperViLoginRequiredMixin
from transaction.models import Invoice, Credit
from transaction.tables import InVoiceTable, CreditTables
from transaction.variables import INVOICE_TYPE_CHOICE


class SellInvoiceListView(StoreKeeperViLoginRequiredMixin ,SingleTableView, ListView):
    model = Invoice
    table_class = InVoiceTable
    template_name = "dashboard/tables.html"
    paginate_by = PAGINATED_BY_VALUE

    def get_queryset(self):
        return Invoice.objects.filter(invoice_type=INVOICE_TYPE_CHOICE[1][0])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creation_link"] = {
            "title": "ایجاد فاکتور فروش جدید",
            "link": reverse("product-create-view")
        }
        context["title"] = "لیست فاکتور های فروش"
        return context


class PurchaseInvoiceListView(StoreKeeperViLoginRequiredMixin ,SingleTableView, ListView):
    model = Invoice
    table_class = InVoiceTable
    template_name = "dashboard/tables.html"
    paginate_by = PAGINATED_BY_VALUE

    def get_queryset(self):
        return Invoice.objects.filter(invoice_type=INVOICE_TYPE_CHOICE[0][0])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creation_link"] = {
            "title": "ایجاد فاکتور خرید جدید",
            "link": reverse("product-create-view")
        }
        context["title"] = "لیست فاکتور های خرید"
        return context

class CreditListView(StoreKeeperViLoginRequiredMixin ,SingleTableView, ListView):
    model = Credit
    table_class = CreditTables
    template_name = "dashboard/tables.html"
    paginate_by = PAGINATED_BY_VALUE

    def get_queryset(self):
        return Credit.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creation_link"] = {
            "title": "ایجاد اعتبار جدید",
            "link": reverse("product-create-view")
        }
        context["title"] = "لیست اعتبارات"
        return context
