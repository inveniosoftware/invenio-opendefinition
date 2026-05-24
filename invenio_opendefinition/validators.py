# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""JSON schema validators."""

import importlib.resources
import json

import jsonschema


def validator_factory(schema_filename):
    """Build a jsonschema validator."""
    with open(schema_filename) as file:
        schema_json = json.load(file)

    return jsonschema.Draft4Validator(schema_json)


license_validator = validator_factory(
    importlib.resources.files("invenio_opendefinition").joinpath(
        "jsonschemas/licenses/license-v1.0.0.json"
    )
)
