# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


COLLATERAL_TYPE_CHOICES = (
    (0, 'Auto'),
    (1, 'Motorcycle'),
)

PRODUCT_TYPE_CHOICES = (
    (0, 'Retail'),
    (1, 'Lease'),
    (2, 'Balloon'),
)

DEAL_TYPE_CHOICES = (
    (0, 'Regular/Digital'),
    (1, 'Spot'),
)

APPLICANT_TYPE_CHOICES = (
    (0, 'Applicant'),
    (1, 'Co-Applicant'),
)


class LenderDetails(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class StateDetails(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lender(models.Model):
    lender = models.ForeignKey(LenderDetails, on_delete=models.CASCADE)
    lender_state = models.ForeignKey(StateDetails, on_delete=models.CASCADE)
    collateral_type = models.IntegerField(
        choices=COLLATERAL_TYPE_CHOICES, default=0)
    product_type = models.IntegerField(choices=PRODUCT_TYPE_CHOICES, default=0)
    deal_type = models.IntegerField(choices=DEAL_TYPE_CHOICES, default=0)
    applicant_type = models.IntegerField(
        choices=APPLICANT_TYPE_CHOICES, default=0)

    def __str__(self):
        return self.lender.name
