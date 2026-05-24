# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""Invenio module integrating Invenio repositories and OpenDefinition."""

from __future__ import absolute_import, print_function

from .ext import InvenioOpenDefinition
from .proxies import current_opendefinition
from .version import __version__

__all__ = (
    "__version__",
    "current_opendefinition",
    "InvenioOpenDefinition",
)
