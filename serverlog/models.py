# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class InstanceLog(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

