#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import create_operation_handler

query = create_operation_handler({
    "method": "GET",
    "url": "/v1/message.query",
    "auth_required": True
})

delete = create_operation_handler({
    "method": "GET",
    "url": "/v1/message.delete",
    "auth_required": True
})

create = create_operation_handler({
    "method": "POST",
    "url": "/v1/message.create",
    "auth_required": True
})

update_text = create_operation_handler({
    "method": "POST",
    "url": "/v1/message.update_text",
    "auth_required": True
})
