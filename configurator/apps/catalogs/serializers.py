"""
Autogenerate serializers file
"""
from rest_framework import serializers
from .models import Status	# pylint: disable=relative-beyond-top-level

class StatusSerializer(serializers.ModelSerializer):
    """
    Status Serialzier
    """

    class Meta: 	# pylint: disable=too-few-public-methods
        """
        Select all fields from model Status
        """

        model = Status
        fields = '__all__'
