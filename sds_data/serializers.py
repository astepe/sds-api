from rest_framework import serializers

from .models import SafetyDataSheet


class SDSSerializer(serializers.ModelSerializer):
    """Serializer for SafetyDataSheet model"""

    class Meta:
        model = SafetyDataSheet
        fields = ('id', 'manufacturer', 'product_name', 'product_code',
                  'flash_point_fahrenheit', 'specific_gravity_g_cm3',
                  'nfpa_fire', 'npfa_health', 'nfpa_reactivity', 'sara_311',
                  'revision_date', 'physical_state', 'cas_number', )
        read_only_fields = ('id', )
