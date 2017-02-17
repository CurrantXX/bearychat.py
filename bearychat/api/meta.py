#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import create_operation_handler

info = create_operation_handler({
    "method": "GET",
    "url": "/v1/meta",
    "auth_required": False
})
