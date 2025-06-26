from django import forms

from warehouse.models import Product, WarehouseItem
from base.forms import BaseForm

class ProductAdminForm(BaseForm):
    class Meta:
        model = Product
        fields = ["name", "price_label", "shell_item_count", "sell_price"]

    def clean(self):
        cleaned_data = super(ProductAdminForm, self).clean()
        price_label = self.cleaned_data["price_label"]
        shell_item_count = self.cleaned_data["shell_item_count"]
        sell_price = self.cleaned_data["sell_price"]

        if all([price_label, shell_item_count, sell_price]):
            if sell_price <= shell_item_count * price_label:
                raise forms.ValidationError("قیمت خرید فروش وارده باید از {} بیشتر باشد".format(shell_item_count * price_label))
        return cleaned_data

class WarehouseItemAdminForm(BaseForm):
    class Meta:
        model = WarehouseItem
        fields = ["product", "stock_level"]