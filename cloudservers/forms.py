

from django.forms import ModelForm

from cloudservers.models import ServerStorageMemory, DeviceMedia


class ServerStorageMemoryForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = ServerStorageMemory
        fields = "__all__"



class MediaFileForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = DeviceMedia
        fields = "__all__"