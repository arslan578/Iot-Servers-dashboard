from django.contrib import admin
from .models import DeviceMedia, ServerStorageMemory
# Register your models here.

admin.site.register(DeviceMedia)
admin.site.register(ServerStorageMemory)