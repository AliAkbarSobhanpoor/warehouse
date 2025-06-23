from django.db import models
from django_jalali.db import models as jmodels
from user.models import User


class Base(models.Model):
    """
    base model for all models
    """
    created_at = jmodels.jDateTimeField(verbose_name="تاریخ ایجاد", auto_now=True)
    updated_at = jmodels.jDateTimeField(verbose_name="تاریخ ویرایش", auto_now=True)
    created_by = models.ForeignKey(
        verbose_name="ایجاد کننده",
        to="user.User",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by"
    )
    updated_by = models.ForeignKey(
        verbose_name="ویرایش کننده",
        to="user.User",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_updated_by"

    )

    class Meta:
        abstract = True