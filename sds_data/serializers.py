from rest_framework import serializers

from .models import SafetyDataSheet, Manufacturer


class SDSSerializer(serializers.ModelSerializer):
    """Serializer for SafetyDataSheet model"""

    manufacturer = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Manufacturer.objects.all()
    )

    class Meta:
        model = SafetyDataSheet
        fields = ('__all__')
        read_only_fields = ('id', )

    def validate_flash_point(self, value):
        """if an invalid entry is given, set to default of NULL"""
        if not isinstance(value, int):
            return
        return value


class ManufacturerSerializer(serializers.ModelSerializer):
    """Serializer for Manufacturer model"""

    class Meta:
        model = Manufacturer
        fields = ('__all__')
        read_only_fields = ('id', )
