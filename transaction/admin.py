from django.contrib import admin
from .models import Invoice, InvoiceItem


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 0
    fields = ('product', 'formated_price', 'count', 'formated_total_price')
    readonly_fields = ('total_price',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Invoice model.
    """
    list_display = ('id', 'customer', 'get_total_invoice_price', 'created_at', 'updated_at')
    list_display_links = ('id', 'customer',)
    search_fields = ('customer__username', 'customer__first_name', 'customer__last_name')
    list_filter = ('created_at', 'updated_at')
    inlines = [InvoiceItemInline]

    def get_total_invoice_price(self, obj):
        return sum(item.total_price for item in obj.invoice_item.all())
    get_total_invoice_price.short_description = "قیمت کل فاکتور"

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for the InvoiceItem model (though often managed via InvoiceInline).
    """
    list_display = ('id', 'invoice', 'product', 'price', 'count', 'total_price', 'created_at', 'updated_at')
    list_display_links = ('id', 'invoice', 'product',)
    readonly_fields = ('total_price',)
    search_fields = ('invoice__id', 'product__name')
    list_filter = ('invoice', 'product', 'created_at', 'updated_at')