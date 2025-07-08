import django_tables2 as tables

from base.functions import thousand_separators
from .functions import get_available_stock_level
from .models import Product


class ProductTable(tables.Table):
    stock_level = tables.Column(empty_values=(), verbose_name="موجودی انبار", orderable=False)

    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "name", "price_label", "shell_item_count", "stock_level",
        )

    def render_price_label(self, value, **kwargs):
        return  thousand_separators(value)

    def render_stock_level(self, record, **kwargs):
        return get_available_stock_level(record.id, None)