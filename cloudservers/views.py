from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from cloudservers.forms import ServerStorageMemoryForm, MediaFileForm
from cloudservers.models import ServerStorageMemory, DeviceMedia
from devices.models import Device
from iotdashboard.settings import LOGIN_URL


# Create your views here.


@login_required(login_url=LOGIN_URL)
def region_key_list(request, server=''):
    """
    :param request:
    :return:
    """
    server = server.capitalize()
    if server == "Lahore":
        lahore_server = True
    elif server == "Islamabad":
        islamabad_server = True

    if server == "London":
        london_server = True

    if server == "Portsmouth":
        portsmouth_server = True
    list = Device.objects.filter(servers=server)
    return render(request, "back/server_device_list.html", locals())


@login_required(login_url=LOGIN_URL)
def servers_memory_monitoring(request, server=''):
    """
    :param request:
    :return:
    """
    memory_monitoring = True
    list = ServerStorageMemory.objects.all()
    return render(request, "back/memory_usage_servers_list.html", locals())


@login_required(login_url=LOGIN_URL)
@csrf_exempt
def server_created(request):
    """
    :param request:
    :return:
    """
    server_add = True
    msg_ok = ""
    msg_err = ""

    if request.method == 'POST':
        form = ServerStorageMemoryForm(request.POST)
        if form.is_valid():
            form.save()
            msg_ok = "Create Server successful"
        else:
            msg_err = "Attention! Please correct the errors!"

    form = ServerStorageMemoryForm()

    return render(request, "back/add.html", locals())


@login_required(login_url=LOGIN_URL)
def increase_or_decrease_memory_memory(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(ServerStorageMemory, id=id)

    form = ServerStorageMemoryForm(request.POST or None, request.FILES or None, instance=val)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg_ok = "Channel update successful"
            return HttpResponseRedirect(reverse('servers_memory_monitoring'))
        else:
            msg_err = "Attention! Please correct the errors"

    return render(request, "back/add.html", locals())


@login_required(login_url=LOGIN_URL)
def delete_memory_servers(request, id=None):
    """
    :param request:
    :param id:
    :return:
    """
    device = get_object_or_404(ServerStorageMemory, id=id).delete()

    msg_ok = "Server deleted"

    return HttpResponseRedirect(reverse('servers_memory_monitoring'), locals())


@login_required(login_url=LOGIN_URL)
def media_files_list(request, server=''):
    """
    :param request:
    :return:
    """
    if server == "Lahore":
        lahore_server_media = True
    elif server == "Islamabad":
        islamabad_server_media = True

    if server == "London":
        london_server_media = True

    if server == "Portsmouth":
        portsmouth_server_media = True

    server_memory = ServerStorageMemory.objects.filter(location=server.capitalize()).first()
    used_memory = server_memory.used_memory
    server_name = server.capitalize()
    list = DeviceMedia.objects.filter(location=server.capitalize())
    return render(request, "back/media_files_list.html", locals())


@login_required(login_url=LOGIN_URL)
def dirty_jeans_media(request):
    """
    :param request:
    :return:
    """

    list = DeviceMedia.objects.filter(is_dirty_jeans=True)
    return render(request, "back/dirty_jeans.html", locals())

@login_required(login_url=LOGIN_URL)
@csrf_exempt
def media_file_add(request):
    """
    :param request:
    :return:
    """
    media_add = True
    msg_ok = ""
    msg_err = ""

    if request.method == 'POST':
        form = MediaFileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

            msg_ok = "Add File successful"
        else:
            msg_err = "Attention! Please correct the errors!"

    form = MediaFileForm()

    return render(request, "back/add.html", locals())


@login_required(login_url=LOGIN_URL)
def media_edit(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(DeviceMedia, id=id)

    form = MediaFileForm(request.POST or None, request.FILES or None, instance=val)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg_ok = "Media File update successful"
            return HttpResponseRedirect(reverse('media_list', kwargs={'server': val.location}))
        else:
            msg_err = "Attention! Please correct the errors"

    return render(request, "back/add.html", locals())


@login_required(login_url=LOGIN_URL)
def media_delete(request, id=None):
    """
    :param request:
    :param id:
    :return:
    """

    device = get_object_or_404(DeviceMedia, id=id)
    location = device.location
    device.delete()

    msg_ok = "File deleted"

    return HttpResponseRedirect(reverse('media_list', kwargs={'server': location}), locals())


@login_required(login_url=LOGIN_URL)
def check_region_server_memory_available(request, server=''):
    """
    :param request:
    :return:
    """
    required_server_memory = ServerStorageMemory.objects.filter(location=server.capitalize()).first()
    list = ServerStorageMemory.objects.filter(region=required_server_memory.region)
    if server == "Lahore":
        lahore_server_media = True
    elif server == "Islamabad":
        islamabad_server_media = True

    if server == "London":
        london_server_media = True

    if server == "Portsmouth":
        portsmouth_server_media = True

    available_memory_servers = True
    server_name = server.capitalize()

    return render(request, "back/memory_usage_servers_list.html", locals())

