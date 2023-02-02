from django.db import models
from django.utils.translation import gettext_lazy as _


class ItemType(models.TextChoices):
    CONSUMIBLE = "CONSUMIBLE", _('Consumible')
    ARMA = "ARMA", _('Arma')
