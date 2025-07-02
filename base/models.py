from django.contrib.auth import get_user_model
from django.db import models
from django_jalali.db import models as jmodels
from simple_history.models import HistoricalRecords

# history models setter and getter -------------------------------------------------------------------------------------

def history_user_getter(historical_instance):
    if historical_instance.history_user_id is None:
        return None

    try:
        return get_user_model().objects.get(id=historical_instance.history_user_id)
    except get_user_model().DoesNotExist:
        return None

def history_suer_setter(historical_instance, user):
    if user is not None:
        historical_instance.history_user_id = user.id
    else:
        historical_instance.history_user_id = None


# ----------------------------------------------------------------------------------------------------------------------


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

    history = HistoricalRecords(
        inherit=True,
        history_user_id_field=models.IntegerField(null=True, blank=True),
        history_user_getter=history_user_getter,
        history_user_setter=history_suer_setter,
    )

    class Meta:
        abstract = True