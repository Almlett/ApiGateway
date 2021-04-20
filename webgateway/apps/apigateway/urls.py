# -*- encoding: utf-8 -*-
"""
"""

from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .viewsets import ProyectViewSet, ApiViewSet, Gateway # pylint: disable=relative-beyond-top-level

router = DefaultRouter()
router.register(r'proyects', ProyectViewSet)
router.register(r'apilist', ApiViewSet)

urlpatterns = [
    re_path(r'api/.*', Gateway.as_view())
]

urlpatterns += router.urls