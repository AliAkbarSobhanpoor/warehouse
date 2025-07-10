"""
    this is the main functions for the . warehouse items.
    all related warehouse items live here.
"""
from transaction.models import InvoiceItem, Credit
from transaction.variables import INVOICE_TYPE_CHOICE, CREDIT_TYPE_CHOICE
from django.db.models import Sum


def get_total_purchase_of_product(product_id: int, exclude_item_id:int | None) -> int:
    total_purchase: int = InvoiceItem.objects.filter(
        product_id=product_id,
        invoice__invoice_type=INVOICE_TYPE_CHOICE[0][0],
    ).exclude(id=exclude_item_id).aggregate(
        total_count=Sum("count", default=0)
    )["total_count"]
    return total_purchase


def get_total_sell_of_product(product_id:int, exclude_item_id:int | None) -> int:
    total_sell: int = InvoiceItem.objects.filter(
        product_id=product_id,
        invoice__invoice_type=INVOICE_TYPE_CHOICE[1][0],
    ).exclude(id=exclude_item_id).aggregate(
        total_count=Sum("count", default=0)
    )["total_count"]
    return total_sell


def get_available_stock_level(product_id:int, exclude_item_id:int | None) -> int:
    """
        returns the current available stock level for given product
        Args:
            product_id (int): the ID of the product for which stock level is to be calculated

        Returns:
            int: the current available stock level for the requested product
    """
    purchased_items: int = get_total_purchase_of_product(product_id, exclude_item_id)
    sell_items: int = get_total_sell_of_product(product_id, exclude_item_id)
    return purchased_items - sell_items # if this return negative value then something is wrong.


def get_customer_total_balance(customer_id:int) -> int:
    positive_credits_total_price = Credit.objects.filter(
        customer_id=customer_id,
        credit_type=CREDIT_TYPE_CHOICE[0][0]
    ).aggregate(positive_total_price=Sum("amount", default=0))["positive_total_price"]
    negative_credits_total_price = Credit.objects.filter(
        customer_id=customer_id,
        credit_type=CREDIT_TYPE_CHOICE[1][0]
    ).aggregate(positive_total_price=Sum("amount", default=0))["positive_total_price"]
    return positive_credits_total_price - negative_credits_total_price