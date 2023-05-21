from django.db import models


class PersonalityOption(models.TextChoices):
    PHYSICAL = "Physical"
    LEGAL = "Legal"
