from django.db import models
from django_jalali.db import models as jmodels
from simple_history.models import HistoricalRecords
from base.models import Base, history_suer_setter, history_user_getter

class Product(Base):
    name = models.CharField(verbose_name="عنوان محصول", max_length=100)
    price_label = models.PositiveIntegerField(verbose_name="قیمت فروش روی محصول",)
    shell_item_count = models.PositiveIntegerField(verbose_name="تعداد آیتم های هر شل")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return "{} {} فروش".format(self.name, self.price_label)
