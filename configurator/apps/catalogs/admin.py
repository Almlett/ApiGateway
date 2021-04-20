"""
Autogenerate admin file
"""
from django.contrib import admin
from .models import Status	# pylint: disable=relative-beyond-top-level

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """
    Status Admin
    """

    fields = (
        "name",
    )
    list_display = (
        "name",
    )
