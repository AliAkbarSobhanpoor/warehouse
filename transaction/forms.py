from django import forms
from django.contrib.auth import get_user_model

from base.forms import BaseForm
from transaction import models
from warehouse.models import Product

class InvoiceAdminForm(BaseForm):
    class Meta:
        model = models.Invoice
        fields = ['customer']

    def __init__(self, *args, **kwargs):
        super(InvoiceAdminForm, self).__init__(*args, **kwargs)
        # exclude the user model itself.
        self.fields["customer"].queryset = get_user_model().objects.exclude(pk=self.user.pk)


class InVoiceItemAdminFrom(BaseForm):
    class Meta:
        model = models.InvoiceItem
        fields = ['invoice', 'product', 'price', 'count']
        # need some validation.

    def clean(self):
        cleaned_data: dict = super().clean()
        # todo: price cat be lower that the sell price that you connected.
        product: Product = cleaned_data.get("product") # can not be None
        count: int = cleaned_data.get("count")
        price: int = cleaned_data.get("price")

        # count can not be grater than product in the product count.
        if count > product.warehouse_item.stock_level:
            self.add_error("count", "مقدار نمیتواند بیشتر از موجودی انبار شما ({}) باشد.".format(product.warehouse_item.stock_level))

        if price <= product.sell_price:
            self.add_error("price", "این قیمت از قیمت وارد شده در محصولات ({}) بیشتر باشد.".format(product.sell_price))

    def save(self, commit=True):
        instance: models.InvoiceItem = super().save(commit=False)
        warehouse_item = instance.product.warehouse_item
        warehouse_item.stock_level -= instance.count
        if commit:
            instance.save()
            warehouse_item.save()
        return instance