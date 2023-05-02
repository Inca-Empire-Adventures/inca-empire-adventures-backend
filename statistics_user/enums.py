from django.db import models
from django.utils.translation import gettext_lazy as _


class EthnicityType(models.TextChoices):
    GOD_OF_SUN = "GOD_OF_SUN", _('Dios del Sol')
    GOD_OF_DEATH = "GOD_OF_DEATH", _('Dios de la Muerte')
    GOD_OF_MOON = "GOD_OF_MOON", _('Dios de la Luna')
    GOD_OF_EARTH = "GOD_OF_EARTH", _('Dios de la Tierra')
