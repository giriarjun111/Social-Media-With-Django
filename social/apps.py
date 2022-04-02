from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SocialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social'

    def ready(self):
        import social.signals
