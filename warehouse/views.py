from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import SingleTableView

from base.views import StoreKeeperViLoginRequiredMixin
from warehouse.models import Product
from warehouse.tables import ProductTable


# Create your views here.

class ProductListView(StoreKeeperViLoginRequiredMixin ,SingleTableView, ListView):
    model = Product
    table_class = ProductTable
    template_name = "dashboard/tables.html"
    paginate_by = 25

    def get_queryset(self):
        return Product.objects.all().order_by("created_at")