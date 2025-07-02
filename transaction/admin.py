from django.contrib import admin

from base.forms import BaseFormSet
from .forms import InvoiceAdminForm, InVoiceItemAdminFrom, CreditAdminForm
from .models import Invoice, InvoiceItem, Credit
from base.admin import BaseModelAdmin

class InvoiceItemInline(admin.TabularInline):
    form = InVoiceItemAdminFrom
    formset = BaseFormSet
    model = InvoiceItem
    extra = 0
    fields = ('product', 'price', 'count', 'total_price')
    readonly_fields = ('total_price',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        class FormSetWithUser(formset):
            def __init__(self_inner, *args, **kwargs_inner):
                kwargs_inner['user'] = request.user
                super().__init__(*args, **kwargs_inner)
        return FormSetWithUser

@admin.register(Invoice)
class InvoiceAdmin(BaseModelAdmin):
    """
    Admin configuration for the Invoice model.
    """
    form = InvoiceAdminForm
    list_display = ('id', 'customer', 'invoice_type' ,'get_total_invoice_price', 'created_at', 'updated_at',)
    list_display_links = ('id', 'customer',)
    search_fields = ('customer__username', 'customer__first_name', 'customer__last_name')
    list_filter = ('created_at', 'updated_at', "invoice_type")
    inlines = [InvoiceItemInline]

    def get_total_invoice_price(self, obj):
        return sum(item.total_price for item in obj.invoice_item.all())
    get_total_invoice_price.short_description = "قیمت کل فاکتور"

@admin.register(InvoiceItem)
class InvoiceItemAdmin(BaseModelAdmin):
    """
    Admin configuration for the InvoiceItem model (though often managed via InvoiceInline).
    """
    form = InVoiceItemAdminFrom
    list_display = ('id', 'invoice', 'product', 'price', 'count', 'total_price', 'created_at', 'updated_at')
    list_display_links = ('id', 'invoice', 'product',)
    readonly_fields = ('total_price',)
    search_fields = ('invoice__id', 'product__name')
    list_filter = ('invoice', 'product', 'created_at', 'updated_at')


@admin.register(Credit)
class CreditAdmin(BaseModelAdmin):
    form = CreditAdminForm
    list_display = ['customer', 'invoice', 'credit_type', 'amount']
