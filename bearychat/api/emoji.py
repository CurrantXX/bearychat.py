#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import create_operation_handler

list = create_operation_handler({
    "method": "GET",
    "url": "/v1/emoji.list",
    "auth_required": True
})
