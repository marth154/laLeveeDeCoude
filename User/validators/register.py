from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_username(value):
    if len(value) <= 5 :
        raise ValidationError(
            _('%(value)s est trop cours'),
            params={'value': value},
        )
    if len(value) >= 215 :
        raise ValidationError(
            _('%(value)s est trop long'),
            params={'value': value},
        )