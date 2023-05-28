from django.db import models
from django.utils.translation import gettext_lazy as _


class EthnicityType(models.TextChoices):
    GOD_OF_SUN = "Dios del Sol", _('Dios del Sol')
    GOD_OF_DEATH = "Dios de la Muerte", _('Dios de la Muerte')
    GOD_OF_MOON = "Dios de la Luna", _('Dios de la Luna')
    GOD_OF_EARTH = "Dios de la Tierra", _('Dios de la Tierra')
