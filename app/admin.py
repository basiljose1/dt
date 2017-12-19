# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import LenderDetails, StateDetails, Lender

# Register your models here.
admin.site.register(LenderDetails)
admin.site.register(StateDetails)
admin.site.register(Lender)
