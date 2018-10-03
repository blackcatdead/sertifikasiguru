# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from sertifikasiguru.models import Sekolah, Kepala, Guru, File, Paket, Order, Subject
# Register your models here.
admin.site.register(Sekolah)
admin.site.register(Kepala)
admin.site.register(Guru)
admin.site.register(File)
admin.site.register(Paket)
admin.site.register(Order)
admin.site.register(Subject)