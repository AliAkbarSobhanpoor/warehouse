from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords
from base.models import Base
from user.variables import ROLES
from warehouse.functions import get_customer_total_balance


class Customer(Base):
    user = models.OneToOneField(verbose_name="اکانت", to="user.User", on_delete=models.PROTECT, null=True, blank=True, related_name="customer_profile")
    role = models.CharField(verbose_name="نقش کاربر", choices=ROLES, max_length=15, default=ROLES[0][0])
    first_name = models.CharField(verbose_name="نام", max_length=200)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=200)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"

    @property
    def customer_total_balance(self):
        "this is come from the balance . but if user has demand then this will be 0"
        total_balance = get_customer_total_balance(self.id)
        return total_balance

class User(AbstractUser):
    pass