from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from cloudservers.forms import ServerStorageMemoryForm
from cloudservers.models import ServerStorageMemory
from devices.models import Device
from iotdashboard.settings import LOGIN_URL

# Create your views here.


@login_required(login_url=LOGIN_URL)
def region_key_list(request, server=''):
    """
    :param request:
    :return:
    """
    if server == "Lahore":
        lahore_server = True
    elif server == "Islamabad":
        islamabad_server = True

    if server == "London":
        london_server = True

    if server == "Portsmouth":
        portsmouth_server = True
    list = Device.objects.filter(servers=server.capitalize())
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
