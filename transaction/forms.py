from django import forms
from django.contrib.auth import get_user_model

from base.forms import BaseForm
from transaction import models
from transaction.functions import get_max_price_for_purchase_a_product
from transaction.variables import INVOICE_TYPE_CHOICE
from warehouse.functions import get_available_stock_level
from warehouse.models import Product


class InvoiceAdminForm(BaseForm):
    class Meta:
        model = models.Invoice
        fields = ['customer', "invoice_type"]

    def __init__(self, *args, **kwargs):
        super(InvoiceAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(InvoiceAdminForm, self).clean()
        customer: get_user_model() = cleaned_data.get("customer")
        invoice_type: str = cleaned_data.get("invoice_type")
        if invoice_type == INVOICE_TYPE_CHOICE[1][0] and customer.id == 1:
            self.add_error("customer", "امکان فروش آیتم به خودتان از شما گرفته شده است.")
        if invoice_type == INVOICE_TYPE_CHOICE[0][0] and customer.id != 1:
            self.add_error("customer", "فعلا فقط امکان خرید برای خود شما وجود دارد. و فاکتور خرید به نام فرد دیگری نمیتوانید تقاضا دهید.")


class InVoiceItemAdminFrom(BaseForm):
    class Meta:
        model = models.InvoiceItem
        fields = ['invoice', 'product', 'price', 'count']

    def clean(self):
        cleaned_data = super(InVoiceItemAdminFrom, self).clean()
        product: Product = cleaned_data.get("product")
        count: int = cleaned_data.get("count")
        invoice: models.Invoice = cleaned_data.get("invoice")
        price: int = cleaned_data.get('price')
        product_available_stock_level: int = get_available_stock_level(product.id)
        max_purchase_price = get_max_price_for_purchase_a_product(product.id)
        if invoice.invoice_type == INVOICE_TYPE_CHOICE[1][0] and count > product_available_stock_level:
            self.add_error("count", "تنها {} شل از {} در انبار موجود است".format(product_available_stock_level, product))
        if price < max_purchase_price:
            self.add_error("price", "قیمت فروش نمیتواند کمتر از بیشترین قیمت خرید ({}) باشد.".format(max_purchase_price))
