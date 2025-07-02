from django.db import models
from django.db.models import F, Sum
from base.models import Base
from user.models import User
from warehouse.models import Product
from transaction.variables import INVOICE_TYPE_CHOICE, CREDIT_TYPE_CHOICE


class Invoice(Base):
    invoice_type = models.CharField(verbose_name="نوع فاکتور", max_length=10, choices=INVOICE_TYPE_CHOICE, default=INVOICE_TYPE_CHOICE[0][0])
    customer = models.ForeignKey(verbose_name="مشتری", to="user.Customer", on_delete=models.PROTECT)

    # we can create a finalized approach here to change the default workspace. and if a factor is not finalized.
    # don't use it in warehouse available items.

    def __str__(self):
        if self.invoice_type == INVOICE_TYPE_CHOICE[0][0]:
            invoice_type = INVOICE_TYPE_CHOICE[0][1]
        else:
            invoice_type = INVOICE_TYPE_CHOICE[1][1]
        return 'فاکتور {} شماره {} کاربر {}'.format(invoice_type, self.id, self.customer)

    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = "فاکتور ها"

    @property
    def calculate_invoice_total_price(self):
        return InvoiceItem.objects.filter(
            invoice=self.id
        ).aggregate(
            total_price=Sum('total_price', default=0)
        )['total_price']


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


class Credit(Base): # after this you can implement a payment. for manual . bank and so on.
    customer = models.ForeignKey(
        verbose_name="مشتری",
        to="user.Customer",
        on_delete=models.PROTECT,
        related_name="credits",
    )
    invoice = models.ForeignKey(
        verbose_name="فاکتور",
        to="transaction.Invoice",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    credit_type = models.CharField( # for purchase a negative credit is created. for payments a positive credit.
        verbose_name="نوع اعتبار",
        max_length=10,
        choices=CREDIT_TYPE_CHOICE,default=CREDIT_TYPE_CHOICE[0][0]
    )
    amount = models.PositiveIntegerField(verbose_name="مقدار اعتبار", default=0)
    reason = models.TextField(verbose_name="توضیحات", help_text="مثلا پرداخت فاکتور، هدیه، اصلاح حساب و ...")

    class Meta:
        verbose_name = "اعتبار"
        verbose_name_plural = "اعتبارات"
        ordering = ['-created_at']
