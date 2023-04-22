from django.db import models

from devices.models import Device, country
from django.utils.translation import ugettext_lazy as _

# Create your models here.



CITIES = (
    ("", ""),
    ("Islamabad", "Islamabad"),
    ("Lahore", "Lahore"),
    ("Karachi", "Karachi"),
    ("London", "London"),
    ("Portsmouth", "Portsmouth"),
    ("Manchester", "Manchester"),

)


# class DeviceMedia(models.Model):
#
#     register_device = models.ForeignKey(_('Region Register Devices'), Device, on_delete=models.CASCADE)
#     file = models.FileField(_('Media Files'), upload_to="files/")
#     dns = models.CharField(_('DNS'),max_length=128)
#     ip_address = models.CharField(_('Region Register Devices'), max_length=32)
#     city = models.CharField(max_length=32,choices=CITIES, default="")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.register_device.name}-{self.ip_address}-{self.created_at}"


class DeviceMedia(models.Model):
    register_device = models.ForeignKey(Device, on_delete=models.CASCADE)
    file = models.FileField(_('Media File'), max_length=256)
    dns = models.CharField(_('DNS'), max_length=128)
    ip_address = models.CharField(_('Ip Address'), max_length=32)
    city = models.CharField(max_length=32, choices=CITIES, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.file_name}-{self.ip_address}"


class ServerStorageMemory(models.Model):
    location = models.CharField(max_length=24, choices=country, default='')
    server_name = models.CharField(max_length=256, default="")
    total_memory = models.FloatField(default=100)
    used_memory = models.FloatField(default=100)
    uploaded_file_limit = models.IntegerField(default=10)
    total_uploaded_file = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


