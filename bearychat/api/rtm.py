#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import create_operation_handler

start = create_operation_handler({
    "method": "GET",
    "url": "/v1/rtm.start",
    "auth_required": True
})
