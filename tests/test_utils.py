# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-License-Identifier: MIT

"""Test utilities."""

from __future__ import absolute_import, print_function

from invenio_opendefinition.loaders import harvest_spdx
from invenio_opendefinition.utils import obj_or_import_string


def test_obj_or_import_string():
    """Test object or string import utility function."""
    assert obj_or_import_string(harvest_spdx) == harvest_spdx
    assert obj_or_import_string(None, default=harvest_spdx) == harvest_spdx
    assert (
        obj_or_import_string("invenio_opendefinition.loaders.harvest_spdx")
        == harvest_spdx
    )
