from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.panel'
    label = 'AdminPanel'
    verbose_name = _('Panel')
