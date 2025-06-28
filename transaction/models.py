from django.db import models
from django.db.models import F, Sum

from base.models import Base
from user.models import User
from warehouse.models import Product


class Invoice(Base):
    customer = models.ForeignKey(verbose_name="مشتری", to="user.User", on_delete=models.PROTECT)

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

    def __str__(self):
        return "آیتم مربوط به {}".format(self.invoice)

    class Meta:
        verbose_name = "آیتم فاکتور"
        verbose_name_plural = "آیتم های فاکتور"
        unique_together = ('invoice', 'product')
