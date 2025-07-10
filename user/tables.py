from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

from base.functions import thousand_separators
from base.tables import BaseTable
from user.models import Customer
from user.variables import CUSTOMER_TABLE_FIELDS
from warehouse.functions import get_customer_total_balance
import django_tables2 as tables

class UserTable(BaseTable):
    class Meta:
        model = get_user_model()
        template_name = "django_tables2/bootstrap4.html"
        fields = ("row_number", "username", "is_superuser")
        exclude = ("created_at_by", "updated_at_by",)

class CustomerTable(BaseTable):
    total_credit = tables.Column(empty_values=(), verbose_name="اعتبار کل", orderable=True)
    class Meta:
        model = Customer
        template_name = "django_tables2/bootstrap4.html"
        fields = ("row_number", *CUSTOMER_TABLE_FIELDS, 'created_at_by', 'updated_at_by', 'operations', )

    def render_total_credit(self, record, **kwargs):
        total_price = get_customer_total_balance(record.id)
        if total_price > 0:
            return mark_safe(
                # language=html
                "<p class='text-success'>{}(طلب کار)</p>".format(thousand_separators(total_price))
            )
        elif total_price < 0 :
            return mark_safe(
                # language=html
                "<p class='text-danger'>{} (بدهکار) </p>".format(thousand_separators(abs(total_price)))
            )
        return thousand_separators(total_price)