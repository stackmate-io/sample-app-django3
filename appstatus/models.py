"""Models for the appstatus app"""
# -*- coding: utf-8 -*-

from django.db import models


class Incident(models.Model):
    """Represents an artist in our collection"""
    title = models.CharField(max_length=255)
    is_resolved = models.BooleanField(default=True)
    occurred_at = models.DateField()
