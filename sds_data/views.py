from rest_framework import viewsets

from .models import SafetyDataSheet
from .serializers import SDSSerializer


class SDSViewSet(viewsets.ModelViewSet):
    """View set for sds data"""
    queryset = SafetyDataSheet.objects.all()
    serializer_class = SDSSerializer
