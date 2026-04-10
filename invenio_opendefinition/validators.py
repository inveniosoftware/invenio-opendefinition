# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

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
