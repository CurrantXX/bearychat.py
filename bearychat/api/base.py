#!/usr/bin/python
# -*- coding: utf-8 -*-
from requests import Request, Session


_base_path = "https://api.bearychat.com"
_token = None


def get_base_path():
    return _base_path


def set_base_path(base_path):
    global _base_path
    _base_path = base_path


def get_auth():
    return _token


def set_auth(token):
    global _token
    _token = token


def do_request(method, url, params=None, json=None):
    req = Request(
        method=method,
        url=url,
        headers={"Accept": "application/json"},
        params=params,
        json=json)

    s = Session()
    prepped = s.prepare_request(req)
    return s.send(prepped)


def create_operation_handler(operation):
    method = operation["method"]
    auth_required = operation["auth_required"]
    relative_url = operation["url"]

    def handler(payload=None):
        payload = {} if payload is None else payload
        if auth_required and "token" not in payload:
            payload["token"] = get_auth()

        url = "{0}{1}".format(get_base_path(), relative_url)

        if method.upper() == "GET":
            return do_request(method, url, payload)
        else:
            return do_request(method, url, json=payload)

    return handler
