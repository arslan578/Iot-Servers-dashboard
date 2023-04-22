import binascii
import os

from django.db import models
from django.utils.translation import ugettext_lazy as _

country = (
    ("", ""),
    ("Pakistan", "Pakistan"),
    ("England", "England"),
    ("Islamabad", "Islamabad"),
    ("Lahore", "Lahore"),
    ("London", "London"),
    ("Portsmouth", "Portsmouth"),

)


class Device(models.Model):
    choices = (
        ("Mobile", "Mobile"),
        ("Laptop", "Laptop"),
        ("Computer", "Computer"),
        ("Tablet", "Tablet"),
        ("Else", "Else"),

    )
    """
    Requests for iot device Gateway
    """
    name = models.CharField(_('Device Name'), max_length=60, help_text=_('Device Name'))
    mac_address = models.CharField(_('Mac Address'), max_length=128)
    location = models.CharField(_('Device Location'), max_length=128, default="")
    device_type = models.CharField(_('Device Type'), choices=choices, max_length=24, default="Mobile")
    servers = models.CharField(_('Cloud Server'), choices=country, max_length=24, default="Portsmouth")
    serial_number = models.CharField(_('Serial Number'), max_length=32)
    api_key = models.CharField(_('Api key'), max_length=200)  # api key
    description = models.TextField(_('Description'), blank=True, max_length=255)
    enable = models.BooleanField(_('Enable'), default=True)
    remote_address = models.CharField(_('Ip Address'), max_length=255)
    pub_date = models.DateTimeField(_('Publish Date'), auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = self.generate_key()

        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(12)).decode()
