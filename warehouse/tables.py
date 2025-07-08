import django_tables2 as tables
from django.utils.safestring import mark_safe
from django.shortcuts import reverse
from base.functions import thousand_separators
from base.tables import BaseTable
from .functions import get_available_stock_level
from .models import Product


class ProductTable(BaseTable):
    stock_level = tables.Column(empty_values=(), verbose_name="موجودی انبار", orderable=False)

    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "row_number", "name", "price_label", "shell_item_count", "stock_level", 'created_at_by', 'updated_at_by',
            'operations',
        )

    def render_price_label(self, value, **kwargs):
        return  thousand_separators(value)

    def render_stock_level(self, record, **kwargs):
        return get_available_stock_level(record.id, None)

    def render_operations(self, record, **kwargs):
        # language=html
        return mark_safe("""
            <a href='{}'>ویرایش</a>
        """.format(reverse("product-update-view", args=[record.id])))