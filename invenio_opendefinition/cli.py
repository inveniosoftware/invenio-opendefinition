# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""Invenio module integrating Invenio repositories and OpenDefinition."""

from __future__ import absolute_import, print_function

import click

from .tasks import harvest_licenses


@click.group()
def opendefinition():
    """Invenio-OpenDefinition commands."""
    pass


@opendefinition.command("loadlicenses")
@click.option("--source", "-s", default="opendefinition")
@click.option("--path", "-p", type=click.Path(exists=True, dir_okay=False))
@click.option("--eager", "-e", is_flag=True)
def loadlicenses(source, path=None, eager=False):
    """Load licenses to local database."""
    click.secho("Loading licenses from {}".format(source), fg="blue")
    task = harvest_licenses.s(source, path=path, eager=eager)
    if eager:
        task.apply(throw=True)
    else:
        task.apply_async()
        click.echo("Loading licenses in a background job.")
