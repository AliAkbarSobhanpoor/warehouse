from django.apps import AppConfig


class TransactionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transaction'

    def ready(self):
        import transaction.signals

    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = "فاتور ها"