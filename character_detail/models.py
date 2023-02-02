from django.db import models
from characters.models import Character
from ethnicity.models import Ethnicity
from professions.models import Profession

# Create your models here.
class CharacterDetail(models.Model):
    character = models.ForeignKey(Character,on_delete=models.SET_NULL, null=True)
    profession = models.ForeignKey(Profession ,on_delete=models.SET_NULL, null=True)
    ethnicity = models.ForeignKey(Ethnicity ,on_delete=models.SET_NULL, null=True)
