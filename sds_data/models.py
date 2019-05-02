from django.db import models
from .validators import validate_cas_format, validate_nfpa_number, \
                        validate_manufacturer_supported


class SafetyDataSheet(models.Model):
    """model for safety data sheet data"""

    # required fields
    manufacturer = models.CharField(max_length=50,
                                  validators=[validate_manufacturer_supported])
    product_name = models.CharField(max_length=50)

    # non-required fields
    product_code = models.CharField(max_length=50, blank=True)

    flash_point_fahrenheit = models.DecimalField(max_digits=6,
                                                 decimal_places=4,
                                                 blank=True)
    specific_gravity_g_cm3 = models.DecimalField(max_digits=6,
                                                 decimal_places=4,
                                                 blank=True)

    nfpa_fire = models.IntegerField(blank=True,
                                    validators=[validate_nfpa_number])
    nfpa_health = models.IntegerField(blank=True,
                                      validators=[validate_nfpa_number])
    nfpa_reactivity = models.IntegerField(blank=True,
                                          validators=[validate_nfpa_number])

    sara_311 = models.CharField(max_length=250, blank=True)
    revision_date = models.DateField(null=True, blank=True)
    physical_state = models.CharField(max_length=25, blank=True)
    cas_number = models.CharField(max_length=12,
                                  blank=True,
                                  validators=[validate_cas_format])

    def __str__(self):
        return f'{self.manufacturer}: {self.product_name} {self.product_code}'
