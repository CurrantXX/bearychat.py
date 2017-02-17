#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import create_operation_handler

info = create_operation_handler({
    "method": "GET",
    "url": "/v1/channel.info",
    "auth_required": True
})

me = create_operation_handler({
    "method": "GET",
    "url": "/v1/user.me",
    "auth_required": True
})

list = create_operation_handler({
    "method": "GET",
    "url": "/v1/user.list",
    "auth_required": True
})
