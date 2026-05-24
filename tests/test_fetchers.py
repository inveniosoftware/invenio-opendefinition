# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""PID Fetchers tests."""

from __future__ import absolute_import, print_function

import uuid

from invenio_opendefinition.fetchers import license_fetcher


def test_license_fetcher():
    """Test license fetcher."""
    val = "MIT"
    pid = license_fetcher(uuid.uuid4(), {"id": val})
    assert pid.provider is None
    assert pid.pid_type is "od_lic"
    assert pid.pid_value is val
