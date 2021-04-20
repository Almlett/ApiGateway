# -*- encoding: utf-8 -*-
"""
Autogenerate urls file
"""
from rest_framework.routers import DefaultRouter
from .viewsets import StatusViewSet # pylint: disable=relative-beyond-top-level

router = DefaultRouter()
router.register(r'status', StatusViewSet)

urlpatterns = router.urls
