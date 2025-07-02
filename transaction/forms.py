from django import forms
from django.contrib.auth import get_user_model

from base.forms import BaseForm
from transaction import models
from warehouse.models import Product

class InvoiceAdminForm(BaseForm):
    class Meta:
        model = models.Invoice
        fields = ['customer', "invoice_type"]

    def __init__(self, *args, **kwargs):
        super(InvoiceAdminForm, self).__init__(*args, **kwargs)
        # exclude the user model itself.


class InVoiceItemAdminFrom(BaseForm):
    class Meta:
        model = models.InvoiceItem
        fields = ['invoice', 'product', 'price', 'count']