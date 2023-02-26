from django.db import models
from django.utils.translation import gettext_lazy as _


class ContentType(models.TextChoices):
    CONTEXTO = "CONTEXTO", _('Contexto')
    ACCION = "ACCION", _('Accion')
    RESULTADO = "RESULTADO", _('Resultado')
