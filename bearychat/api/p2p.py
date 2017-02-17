#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import create_operation_handler

info = create_operation_handler({
    "method": "GET",
    "url": "/v1/p2p.info",
    "auth_required": True
})

list = create_operation_handler({
    "method": "GET",
    "url": "/v1/p2p.list",
    "auth_required": True
})

create = create_operation_handler({
    "method": "POST",
    "url": "/v1/p2p.create",
    "auth_required": True
})
