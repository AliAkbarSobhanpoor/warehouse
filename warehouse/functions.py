"""
    this is the main functions for the . warehouse items.
    all related warehouse items live here.
"""
from transaction.models import InvoiceItem
from transaction.variables import INVOICE_TYPE_CHOICE
from django.db.models import Sum

def get_total_purchase_of_product(product_id: int) -> int:
    total_purchase: int = InvoiceItem.objects.filter(
        product_id=product_id,
        invoice__invoice_type=INVOICE_TYPE_CHOICE[0][0],
    ).aggregate(
        total_count=Sum("count", default=0)
    )["total_count"]
    return total_purchase

def get_total_sell_of_product(product_id:int) -> int:
    total_sell: int = InvoiceItem.objects.filter(
        product_id=product_id,
        invoice__invoice_type=INVOICE_TYPE_CHOICE[1][0],
    ).aggregate(
        total_count=Sum("count", default=0)
    )["total_count"]
    return total_sell

def get_available_stock_level(product_id:int) -> int:
    """
        returns the current available stock level for given product
        Args:
            product_id (int): the ID of the product for which stock level is to be calculated

        Returns:
            int: the current available stock level for the requested product
    """
    purchased_items: int = get_total_purchase_of_product(product_id)
    sell_items: int = get_total_sell_of_product(product_id)
    return purchased_items - sell_items # if this return negative value then something is wrong.
