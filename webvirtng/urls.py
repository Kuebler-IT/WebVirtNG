from django.conf.urls import url
from django.contrib.auth import views as auth_views

from servers import views as servers_views
from hostdetail import views as hostdetail_views
from create import views as create_views
from storages import views as storages_views
from networks import views as networks_views
from interfaces import views as interfaces_views
from instance import views as instance_views
from secrets import views as secrets_views
from console import views as console_views

urlpatterns = [
    url(r'^$', servers_views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^servers/$', servers_views.servers_list, name='servers_list'),
    url(r'^infrastructure/$', servers_views.infrastructure, name='infrastructure'),
    url(r'^host/(\d+)/$', hostdetail_views.overview, name='overview'),
    url(r'^create/(\d+)/$', create_views.create, name='create'),
    url(r'^storages/(\d+)/$', storages_views.storages, name='storages'),
    url(r'^storage/(\d+)/([\w\-\.]+)/$', storages_views.storage, name='storage'),
    url(r'^networks/(\d+)/$', networks_views.networks, name='networks'),
    url(r'^network/(\d+)/([\w\-\.]+)/$', networks_views.network, name='network'),
    url(r'^interfaces/(\d+)/$', interfaces_views.interfaces, name='interfaces'),
    url(r'^interface/(\d+)/([\w\.\:]+)/$', interfaces_views.interface, name='interface'),
    url(r'^instance/(\d+)/([\w\-\.\_]+)/$', instance_views.instance, name='instance'),
    url(r'^instances/(\d+)/$', instance_views.instances, name='instances'),
    url(r'^secrets/(\d+)/$', secrets_views.secrets, name='secrets'),
    url(r'^console/$', console_views.console, name='console'),
    url(r'^info/hostusage/(\d+)/$', hostdetail_views.hostusage, name='hostusage'),
    url(r'^info/insts_status/(\d+)/$', instance_views.insts_status, name='insts_status'),
    url(r'^info/inst_status/(\d+)/([\w\-\.]+)/$', instance_views.inst_status, name='inst_status'),
    url(r'^info/instusage/(\d+)/([\w\-\.]+)/$', instance_views.instusage, name='instusage'),
]

