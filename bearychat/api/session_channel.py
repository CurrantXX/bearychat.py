#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import create_operation_handler

info = create_operation_handler({
    "method": "GET",
    "url": "/v1/sesson_channel.info",
    "auth_required": True
})

list = create_operation_handler({
    "method": "GET",
    "url": "/v1/sesson_channel.list",
    "auth_required": True
})

create = create_operation_handler({
    "method": "POST",
    "url": "/v1/sesson_channel.create",
    "auth_required": True
})

archive = create_operation_handler({
    "method": "POST",
    "url": "/v1/sesson_channel.archive",
    "auth_required": True
})

convert_to_channel = create_operation_handler({
    "method": "POST",
    "url": "/v1/sesson_channel.convert_to_channel",
    "auth_required": True
})

leave = create_operation_handler({
    "method": "POST",
    "url": "/v1/sesson_channel.leave",
    "auth_required": True
})

invite = create_operation_handler({
    "method": "POST",
    "url": "/v1/sesson_channel.invite",
    "auth_required": True
})

kick = create_operation_handler({
    "method": "POST",
    "url": "/v1/sesson_channel.kick",
    "auth_required": True
})
