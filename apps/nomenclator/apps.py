from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NomenclatorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.nomenclator'
    label = 'Nomenclators'
    verbose_name = _('Nomenclador')
    verbose_name_plural = _('Nomencladores')
