from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "bookstore_project.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import bookstore_project.users.signals  # noqa F401
        except ImportError:
            pass
