

from django.forms import ModelForm

from devices.models import Device


class DeviceForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Device
        fields = [
            'name',
            'description',
            'mac_address',
            'location',
            'servers',
            'device_type',
            'serial_number',
            'enable',
        ]

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            if i not in ['enable']:
                self.fields[i].widget.attrs['class'] = 'form-control'
