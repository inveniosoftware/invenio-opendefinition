# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""Test schema."""

from __future__ import absolute_import, print_function

from invenio_opendefinition.validators import license_validator


def test_licenses_schema(od_licenses_json):
    """Test that license schema validates the example file."""
    for key in od_licenses_json:
        license_validator.validate(od_licenses_json[key])
