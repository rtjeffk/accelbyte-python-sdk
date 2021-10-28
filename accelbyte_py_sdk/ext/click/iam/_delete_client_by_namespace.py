import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import delete_client_by_namespace as delete_client_by_namespace_internal


@click.command()
@click.argument("client_id", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def delete_client_by_namespace(
        client_id: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(delete_client_by_namespace_internal.__doc__)
    result, error = delete_client_by_namespace_internal(
        client_id=client_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"DeleteClientByNamespace failed: {str(error)}")
    click.echo("DeleteClientByNamespace success")