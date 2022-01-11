from django.contrib import admin
from django.contrib.admin.models import LogEntry


admin.site.register(LogEntry)
admin.site.site_header = "Sitio web de Servivip"
admin.site.site_title = "Portal de Servivip"
admin.site.index_title = "Bienvenidos al portal de administración de Servivip"