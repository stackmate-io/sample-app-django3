"""Models for the appstatus app"""
# -*- coding: utf-8 -*-
from django.shortcuts import render
from appstatus.models import Incident


def index(request):
    """The application's homepage"""
    return render(request, 'incidents/index.html', {
        'incidents': Incident.objects.order_by('-occurred_at'),
    })
