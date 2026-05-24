# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""Record modification prior to indexing."""

from __future__ import absolute_import, print_function


def indexer_receiver(sender, json=None, record=None, index=None, **dummy_kwargs):
    """Connect to before_record_index signal to transform record for ES."""
    if index.startswith("licenses-"):
        json["suggest"] = {"input": [json["id"], json["title"]]}
