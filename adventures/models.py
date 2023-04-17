from django.db import models
from adventures.enums import RoleType

from characters.models import Character

# Create your models here.
class Adventures(models.Model):
    description = models.TextField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)

class Conversation(models.Model):
    adventure = models.ForeignKey(Adventures, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=RoleType.choices)
    content = models.TextField()
