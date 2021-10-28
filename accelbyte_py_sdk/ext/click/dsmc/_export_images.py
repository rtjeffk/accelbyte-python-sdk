import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.dsmc import export_images as export_images_internal
from ....api.dsmc.models import ModelsImageRecord
from ....api.dsmc.models import ResponseError


@click.command()
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def export_images(
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(export_images_internal.__doc__)
    result, error = export_images_internal(
        namespace=namespace,
    )
    if error:
        raise Exception(f"ExportImages failed: {str(error)}")
    click.echo("ExportImages success")