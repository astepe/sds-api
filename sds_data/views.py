from rest_framework import viewsets
from rest_framework import permissions

from .models import SafetyDataSheet, Manufacturer
from .serializers import SDSSerializer, ManufacturerSerializer


class SDSViewSet(viewsets.ModelViewSet):
    """View set for sds data"""
    queryset = SafetyDataSheet.objects.all()
    serializer_class = SDSSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ManufacturerViewSet(viewsets.ModelViewSet):
    """View set for manufacturers"""
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
