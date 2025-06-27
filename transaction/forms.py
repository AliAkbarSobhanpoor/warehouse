from django import forms
from django.contrib.auth import get_user_model

from base.forms import BaseForm
from transaction import models


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

