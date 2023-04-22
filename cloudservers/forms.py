

from django.forms import ModelForm

from cloudservers.models import ServerStorageMemory


class ServerStorageMemoryForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = ServerStorageMemory
        fields = "__all__"
