"""
    this is the base place for the transaction functions.
"""
from django.db.models import Max

from transaction.models import InvoiceItem
from transaction.variables import INVOICE_TYPE_CHOICE

def get_max_price_for_purchase_a_product(product_id:int) -> int:
    return InvoiceItem.objects.filter(
        product_id=product_id,
        invoice__invoice_type=INVOICE_TYPE_CHOICE[0][0],
    ).aggregate(max_price=Max('price'))['max_price']