from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 1. Create models to store:
#
# A. “Farm” data model - name
# B. “Field” data model - name, farm (ref)
# C. “FieldCrop” data model - variety, field (ref)
# (Read Setup1 to create the data)
# D. Irrigation data from the sheet - LatestOutput and all sheets after that)
#
# 2. Parse the excel sheet to store Farm, Field, FieldCrop and Irrigation data
# 3. Design, develop API to serve the output (please use DRF)
# 4. Frontend to show irrigation schedule for a particular grower, field, variety combination - table and chart


class Farm(models.Model):
    name = models.CharField(max_length=15)


class Field(models.Model):
    name = models.CharField(max_length=15)
    farm = models.ForeignKey(Farm)


class FieldCrop(models.Model):
    name = models.CharField(max_length=15)
    field = models.ForeignKey(Field)


class Irrigation(models.Model):
    fieldcrop = models.ForeignKey(FieldCrop)
    curr_smd = models.DecimalField(decimal_places=3, max_digits=20, null=True)
    lw_smd = models.DecimalField(decimal_places=3, max_digits=20, null=True)
    water_use = models.DecimalField(decimal_places=3, max_digits=20, null=True)
    drainage = models.DecimalField(decimal_places=3, max_digits=20, null=True)
    allowable_smd = models.DecimalField(decimal_places=3, max_digits=20, null=True)
