__author__ = 'karishma'
from rest_framework import serializers
from .models import Irrigation


class IrrigationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Irrigation
        fields = '__all__'