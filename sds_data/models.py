from django.db import models
from .validators import validate_cas_format, validate_nfpa_number, \
                        validate_manufacturer


class Manufacturer(models.Model):
    """Model for Manufacturers"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SafetyDataSheet(models.Model):
    """model for safety data sheet data"""

    # required fields
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=50)

    # non-required fields
    product_code = models.CharField(max_length=50, blank=True)

    flash_point = models.DecimalField(blank=True,
                                      decimal_places=4,
                                      max_digits=6,
                                      null=True)

    specific_gravity = models.DecimalField(blank=True,
                                           decimal_places=4,
                                           max_digits=6,
                                           null=True)

    nfpa_fire = models.IntegerField(blank=True,
                                    null=True,
                                    validators=[validate_nfpa_number])

    nfpa_health = models.IntegerField(blank=True,
                                      null=True,
                                      validators=[validate_nfpa_number])

    nfpa_reactivity = models.IntegerField(blank=True,
                                          null=True,
                                          validators=[validate_nfpa_number])

    sara_311 = models.CharField(max_length=250, blank=True)
    revision_date = models.CharField(max_length=25, blank=True)
    physical_state = models.CharField(max_length=25, blank=True)

    cas_number = models.CharField(max_length=12,
                                  blank=True,
                                  validators=[validate_cas_format])

    last_edit = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.manufacturer}: {self.product_name} {self.product_code}'
