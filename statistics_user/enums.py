from django.db import models
from django.utils.translation import gettext_lazy as _


class EthnicityType(models.TextChoices):
    GOD_OF_SUN = "GOD_OF_SUN", _('God of Sun')
    GOD_OF_DEATH = "GOD_OF_DEATH", _('God of Death')
    GOD_OF_MOON = "GOD_OF_MOON", _('God of Moon')
    GOD_OF_EARTH = "GOD_OF_EARTH", _('God of Earth')
