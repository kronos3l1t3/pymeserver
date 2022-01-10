from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class PanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.panel'
    label = 'AdminPanel'
    verbose_name = _('Panel')

    def ready(self):
        user = get_user_model()
        if not user.objects.all().exists():
            from django.contrib.auth.models import User

            panel_user_name = "Yaniela"
            panel_user_email = "navegabit.2020@gmail.com"
            panel_password = "Fisyb8o9h*"

            superuser = User.objects.create_superuser(
                username=panel_user_name,
                email=panel_user_email,
                password=panel_password
            )

            superuser.save()
