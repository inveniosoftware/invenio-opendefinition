# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT


"""Minimal Flask application example for development.

Run example development server:

.. code-block:: console

   $ cd examples
   $ flask -a app.py --debug run
"""

from __future__ import absolute_import, print_function

from flask import Flask

from invenio_opendefinition import InvenioOpenDefinition

# Create Flask application
app = Flask(__name__)
InvenioOpenDefinition(app)
