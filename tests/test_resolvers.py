# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""Test resolvers."""

from __future__ import absolute_import, print_function

from jsonref import JsonRef
from jsonresolver import JSONResolver
from jsonresolver.contrib.jsonref import json_loader_factory


def test_license_jsonref_resolver(app, loaded_example_licenses):
    """Test resolver."""
    with app.app_context():
        example_license = {
            "license": {"$ref": "http://inveniosoftware.org/licenses/mit"}
        }

        json_resolver = JSONResolver(plugins=["invenio_opendefinition.resolvers"])
        loader_cls = json_loader_factory(json_resolver)
        loader = loader_cls()
        out_json = JsonRef.replace_refs(example_license, loader=loader)
        assert out_json["license"] == loaded_example_licenses["MIT"]
