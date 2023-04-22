"""
"""

from django.urls import path, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from rest_framework import routers

from devices import views as devices

from cloudservers import views as servers

from datas import views as datas

router = routers.DefaultRouter()

urlpatterns = i18n_patterns(
    # dashboard panels index page
    path('', devices.index, name='index'),

    # device api key
    path('key/list/', devices.key_list, name='key_list'),
    path('key/generate/<str:id>/', devices.generate_key, name='generate_key'),

    # add device
    path('device/add/', devices.device_add, name='device_add'),
    path('device/list/', devices.device_list, name='device_list'),
    path('device/edit/<str:id>/', devices.device_edit, name='device_edit'),
    path('device/delete/<str:id>/', devices.device_delete, name='device_delete'),

    # data query
    path('datas/', datas.datalist, name='datas'),
    path('datas/chart/<str:id>/', datas.data_chart, name='data_chart'),
    path('datas/chart/ajax/<str:id>/', datas.data_chart_ajax, name='data_chart_ajax'),

    # export xls
    path('export/<str:model>/', devices.export, name='export'),

    # django admin page
    path('admin/', admin.site.urls),
)

# Cloud Servers

urlpatterns += [
    path('servers/list/<str:server>/', servers.region_key_list, name='region_key_list'),
    path('servers_memory_monitoring/create/', servers.server_created, name='server_created'),
    path('servers_memory_monitoring/', servers.servers_memory_monitoring, name='servers_memory_monitoring'),
    path('servers_memory_monitoring/edit/<str:id>/', servers.increase_or_decrease_memory_memory,
         name='increase_or_decrease_memory_memory'),
    path('servers_memory_monitoring/delete/<str:id>/', servers.delete_memory_servers, name='delete_memory_servers'),
]

urlpatterns += [
    # REST framework
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/datas/', datas.DataList.as_view(), name='api_data'),
    path('api/datas/<int:pk>/', datas.DataDetail.as_view(), name='api_data_detail'),
]

urlpatterns += [
    path('media/<str:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<str:path>/', serve, {'document_root': settings.STATIC_ROOT, }),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
