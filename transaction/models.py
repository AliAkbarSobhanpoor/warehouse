from django.db import models
from django.db.models import F, Sum
from simple_history.models import HistoricalRecords

from base.models import Base, history_suer_setter, history_user_getter
from user.models import User
from warehouse.models import Product
from transaction.variables import INVOICE_TYPE_CHOICE

class Invoice(Base):
    invoice_type = models.CharField(verbose_name="نوع فاکتور", max_length=10, choices=INVOICE_TYPE_CHOICE, default=INVOICE_TYPE_CHOICE[0][0])
    customer = models.ForeignKey(verbose_name="مشتری", to="user.User", on_delete=models.PROTECT) # buy invoice customer always is me.

    # we can create a finalized approach here to change the default workspace. and if a factor is not finalized.
    # don't use it in warehouse available items.

    history = HistoricalRecords(
        history_user_id_field=models.IntegerField(null=True, blank=True),
        history_user_getter=history_user_getter,
        history_user_setter=history_suer_setter,
    )

    def __str__(self):
        return 'فاکتور شماره {} کاربر {}'.format(self.id, self.customer)

    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = "فاکتور ها"


class InvoiceItem(Base):
    invoice = models.ForeignKey(verbose_name="فاکتور", to="transaction.Invoice", on_delete=models.PROTECT, related_name="invoice_item")
    product = models.ForeignKey(verbose_name="محصول", to="warehouse.Product", on_delete=models.PROTECT, related_name="product_invoice_item")
    price = models.PositiveIntegerField(verbose_name="قیمت هر شل", default=0)
    count = models.PositiveIntegerField(verbose_name="تعداد شل", default=0)
    total_price = models.GeneratedField(
        verbose_name="قیمت کل",
        expression=F("price") * F("count"),
        output_field=models.PositiveIntegerField(),
        db_persist=False,
    )
    history = HistoricalRecords(
        history_user_id_field=models.IntegerField(null=True, blank=True),
        history_user_getter=history_user_getter,
        history_user_setter=history_suer_setter,
    )

    def __str__(self):
        return "آیتم مربوط به {}".format(self.invoice)

    class Meta:
        verbose_name = "آیتم فاکتور"
        verbose_name_plural = "آیتم های فاکتور"
        unique_together = ('invoice', 'product')
