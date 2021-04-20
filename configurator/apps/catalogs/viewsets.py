"""
Autogenerate viewsets file
"""
from rest_framework import viewsets
from .models import Status 	# pylint: disable=relative-beyond-top-level
from .serializers import StatusSerializer # pylint: disable=relative-beyond-top-level

class StatusViewSet(viewsets.ModelViewSet):	# pylint: disable=too-many-ancestors
    """
    Status ViewSet
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
