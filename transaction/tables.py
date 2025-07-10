import django_tables2 as tables
from django.utils.safestring import mark_safe

from base.tables import BaseTable
from transaction.models import Invoice, Credit
from transaction.variables import INVOICE_TABLE_FIELDS, CREDIT_TABLE_FIELDS, CREDIT_TYPE_CHOICE


class InVoiceTable(BaseTable):
    get_total_invoice_price = tables.Column(empty_values=(), verbose_name="قیمت کل فاکتور")

    class Meta:
        model = Invoice
        template_name = "django_tables2/bootstrap4.html"
        fields = ("row_number", *INVOICE_TABLE_FIELDS, 'created_at_by', 'updated_at_by', 'operations', )

    def render_get_total_invoice_price(self, **kwargs):
        record = kwargs.get("record")
        return sum(item.total_price for item in record.invoice_item.all())


class CreditTables(BaseTable):
    class Meta:
        model = Credit
        template_name = "django_tables2/bootstrap4.html"
        fields = ("row_number", *CREDIT_TABLE_FIELDS, 'created_at_by', 'updated_at_by', 'operations', )

    def render_amount(self, value, record, **kwargs):
        if record.credit_type == CREDIT_TYPE_CHOICE[0][0]:
            return mark_safe(
                # language=html
                "<p class='text-success'>{}</p>".format(value)
            )
        else:
            return mark_safe(
                # language=html
                "<p class='text-danger'>{}</p>".format(value)
            )