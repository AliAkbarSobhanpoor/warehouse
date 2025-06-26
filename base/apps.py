from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    class Meta:
        verbose_name = 'انبار'
        verbose_name_plural = 'انبار ها'