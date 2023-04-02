from django.db import models
from django.utils.translation import gettext_lazy as _

class RoleType(models.TextChoices):
    SYSTEM  = "system", _('system')
    ASSISTANT  = "assistant", _('assistant')
    USER = "user", _('user')