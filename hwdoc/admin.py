# -*- coding: utf-8 -*- vim:encoding=utf-8:
# vim: tabstop=4:shiftwidth=4:softtabstop=4:expandtab

# Copyright © 2010-2012 Greek Research and Technology Network (GRNET S.A.)
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
# TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
# USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
# OF THIS SOFTWARE.

from django.contrib import admin
from servermon.hwdoc.models import *

admin.site.register(Vendor)
admin.site.register(Model)

class ServerManagementInline(admin.StackedInline):
    model = ServerManagement

class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ['rack', 'unit', 'serial',]

    def mgmt_method(obj):
        return obj.servermanagement.get_method_display()
    mgmt_method.short_description = 'OOB Method'

    def mgmt_username(obj):
        return obj.servermanagement.username
    mgmt_username.short_description = 'OOB Username'

    def mgmt_password(obj):
        return obj.servermanagement.password
    mgmt_password.short_description = 'OOB Password'

    def model_u(obj):
        return obj.model.u
    model_u.short_description = 'Unit Height'

    list_display = ('purpose', 'model', 'serial',
            'rack', 'unit', model_u,
            mgmt_method, mgmt_username, mgmt_password,
            'comments', 'updated', 'state')
    list_display_links = ('serial',)
    list_filter = ('model', 'rack','state',)
    ordering = ('rack', 'unit',)
    inlines = [ ServerManagementInline, ]

admin.site.register(Equipment, EquipmentAdmin)
