from django.db import models
from django_jalali.db import models as jmodels
from simple_history.models import HistoricalRecords
from base.models import Base, history_suer_setter, history_user_getter

class Product(Base):
    name = models.CharField(verbose_name="عنوان محصول", max_length=100)
    price_label = models.PositiveIntegerField(verbose_name="قیمت فروش روی محصول",)
    shell_item_count = models.PositiveIntegerField(verbose_name="تعداد آیتم های هر شل")
    sell_price = models.PositiveIntegerField(
        verbose_name="قیمت فروش",
        help_text="مقدار این فیلد به شما کمک خواهد کرد تا از فروش به قیمت کمتر از این مقدار جلوگیری بکنید",
    )

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return "{} {} فروش".format(self.name, self.price_label)

class WarehouseItem(Base):
    """
    based on the products . we have items in here.
    """
    product = models.OneToOneField(
        "warehouse.Product",
        verbose_name="محصول",
        on_delete=models.PROTECT,
        related_name="warehouse_item",
        unique=True,
    )

    class Meta:
        verbose_name = "دارایی انبار"
        verbose_name_plural = "دارایی های انبار"

    def __str__(self):
        return "{} {} فروش".format(self.product.name, self.product.price_label)