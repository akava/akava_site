from django.contrib import admin
from request_proxy.models import Proxy


class ProxyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'url']
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Proxy, ProxyAdmin)