from django import forms

from warehouse.models import Product
from base.forms import BaseForm

class ProductAdminForm(BaseForm):
    class Meta:
        model = Product
        fields = ["name", "price_label", "shell_item_count"]


class ProductForm(ProductAdminForm):
    class Meta(ProductAdminForm.Meta):
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price_label": forms.TextInput(attrs={
                "class": "form-control number-input",
            }),
            "shell_item_count": forms.NumberInput(attrs={"class": "form-control",}),
        }