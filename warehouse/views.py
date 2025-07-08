from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django_tables2 import SingleTableView

from base.views import StoreKeeperViLoginRequiredMixin, BaseFormView
from warehouse.forms import ProductForm
from warehouse.models import Product
from warehouse.tables import ProductTable

class ProductListView(StoreKeeperViLoginRequiredMixin ,SingleTableView, ListView):
    model = Product
    table_class = ProductTable
    template_name = "dashboard/tables.html"
    paginate_by = 25

    def get_queryset(self):
        return Product.objects.all().order_by("created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creation_link"] = {
            "title": "ایجاد محصول جدید",
            "link": reverse("product-create-view")
        }
        context["title"] = "لیست محصولات"
        return context

class ProductCreateAndUpdateView(StoreKeeperViLoginRequiredMixin, BaseFormView):
    template_name = "dashboard/forms.html"
    form_class = ProductForm
    success_url = reverse_lazy("product-list-view")

    def dispatch(self, request, *args, **kwargs):
        self.object = None
        if "product_id" in self.kwargs:
            self.object = get_object_or_404(Product, pk=self.kwargs["product_id"])
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        if self.object is not None:
            for field in self.form_class.Meta.fields:
                initial[field] = getattr(self.object, field)
        return initial

    def form_valid(self, form):
        if self.object:
            # Update mode
            for field, value in form.cleaned_data.items():
                setattr(self.object, field, value)
            self.object.save()
        else:
            # Create mode
            self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = self.object is not None
        return context