import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import update_google_p12_file as update_google_p12_file_internal
from ....api.platform.models import GoogleIAPConfigInfo


@click.command()
@click.option("--file", "file", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def update_google_p12_file(
        file: Optional[str] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(update_google_p12_file_internal.__doc__)
    try:
        file_json = json.loads(file)
        file = Any.create_from_dict(file_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'file'. {str(e)}")
    result, error = update_google_p12_file_internal(
        file=file,
        namespace=namespace,
    )
    if error:
        raise Exception(f"updateGoogleP12File failed: {str(error)}")
    click.echo("updateGoogleP12File success")