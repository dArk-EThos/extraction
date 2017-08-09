__author__ = 'karishma'
from rest_framework import viewsets
from .models import Irrigation
from .serializers import IrrigationSerializer


class IrrigationViewset(viewsets.ModelViewSet):
    queryset = Irrigation.objects.all()
    serializer_class = IrrigationSerializer

