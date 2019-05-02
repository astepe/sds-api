from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
from sdsparser import manufacturers


def validate_cas_format(value):
    """Validate that the given CAS number follows CAS# format"""
    regex = re.compile(r'^\d{2,7}-\d{2}-\d$')
    if not regex.fullmatch(value):
        raise ValidationError(
            _('%(value)s is not a valid CAS number'),
            params={'value': value},
        )


def validate_nfpa_number(value):
    """Validate that the given number is between 0 and 4"""
    if not 0 <= value <= 4:
        raise ValidationError(
            _('%(value)s is not a valid nfpa number'),
            params={'value': str(value)}
        )


def validate_manufacturer_supported(manufacturer):
    """Validate that the entered value is a currently supported manufacturer"""

    if manufacturer not in manufacturers:
        raise ValidationError(
            _('%(manufacturer)s is not a currently supported manufacturer'),
            params={'manufacturer': manufacturer}
        )
