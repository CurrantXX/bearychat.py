#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import create_operation_handler

info = create_operation_handler({
    "method": "GET",
    "url": "/v1/channel.info",
    "auth_required": True
})
list = create_operation_handler({
    "method": "GET",
    "url": "/v1/channel.list",
    "auth_required": True
})
create = create_operation_handler({
    "method": "POST",
    "url": "/v1/channel.create",
    "auth_required": True
})
invite = create_operation_handler({
    "method": "POST",
    "url": "/v1/channel.invite",
    "auth_required": True
})
archive = create_operation_handler({
    "method": "POST",
    "url": "/v1/channel.archive",
    "auth_required": True
})
unarchive = create_operation_handler({
    "method": "POST",
    "url": "/v1/channel.unarchive",
    "auth_required": True
})
kick = create_operation_handler({
    "method": "POST",
    "url": "/v1/channel.kick",
    "auth_required": True
})
leave = create_operation_handler({
    "method": "POST",
    "url": "/v1/channel.leave",
    "auth_required": True
})
