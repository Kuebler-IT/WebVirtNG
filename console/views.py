# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from instance.models import Instance
from vrtManager.instance import wvmInstance
from webvirtng.settings import WS_PORT, WS_PUBLIC_HOST

import re


def console(request):
    if not request.user.is_authenticated():
        return redirect('login')

    if request.method == 'GET':
        token = request.GET.get('token', '')

    try:
        temptoken = token.split('-', 1)
        host = int(temptoken[0])
        uuid = temptoken[1]
        instance = Instance.objects.get(compute_id=host, uuid=uuid)
        conn = wvmInstance(instance.compute.hostname,
                           instance.compute.login,
                           instance.compute.password,
                           instance.compute.type,
                           instance.name)
        console_type = conn.get_console_type()
        console_websocket_port = conn.get_console_websocket_port()
        console_passwd = conn.get_console_passwd()
    except:
        console_type = None
        console_websocket_port = None
        console_passwd = None

    ws_port = console_websocket_port if console_websocket_port else WS_PORT
    ws_host = WS_PUBLIC_HOST if WS_PUBLIC_HOST else request.get_host()

    if ':' in ws_host:
        ws_host = re.sub(':[0-9]+', '', ws_host)

    if console_type == 'vnc':
        response = render(request, 'console-vnc.html', locals())
    elif console_type == 'spice':
        response = render(request, 'console-spice.html', locals())
    else:
        response = "Console type %s no support" % console_type

    response.set_cookie('token', token)
    return response
