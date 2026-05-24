# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-License-Identifier: MIT

"""Proxy to the current module."""

from __future__ import absolute_import, print_function

from flask import current_app
from werkzeug.local import LocalProxy

current_opendefinition = LocalProxy(
    lambda: current_app.extensions["invenio-opendefinition"]
)
