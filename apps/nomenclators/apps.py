from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NomenclatorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.nomenclators'
    label = 'Nomenclators'
    verbose_name = _('Nomencladores')
