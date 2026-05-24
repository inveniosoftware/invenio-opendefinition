# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""PID fetchers for Invenio-OpenDefinition."""

from __future__ import absolute_import, print_function

from invenio_pidstore.fetchers import FetchedPID


def license_fetcher(record_uuid, data):
    """Fetch PID from license record."""
    return FetchedPID(provider=None, pid_type="od_lic", pid_value=str(data["id"]))
