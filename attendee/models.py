from django.db import models
from django.core.validators import (
    validate_email,
    validate_slug,
    MinLengthValidator,
    MaxLengthValidator
)

# Create your models here.
class Attendee(models.Model):
    # properties
    MIN_NAME_LEN = 1
    MAX_NAME_LEN = 64
    MAX_PHONE_LEN = 14
    MIN_PHONE_LEN = 10

    name  = models.CharField(
        max_length = MAX_NAME_LEN,
        validators = [
            MinLengthValidator,
            MaxLengthValidator
        ]
    )
    email = models.EmailField(
        unique = True,
        validators = [
            validate_email
        ]
    )
    phone = models.CharField(
        unique = True,
        max_length = MAX_PHONE_LEN,
        validators = [
            validate_slug,
            MinLengthValidator,
            MaxLengthValidator
        ]
    )

    class Meta:
        verbose_name = 'attendee table'
        verbose_name_plural = verbose_name