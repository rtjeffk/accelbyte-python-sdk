import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import delete_role as delete_role_internal


@click.command()
@click.argument("role_id", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def delete_role(
        role_id: str,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(delete_role_internal.__doc__)
    result, error = delete_role_internal(
        role_id=role_id,
    )
    if error:
        raise Exception(f"DeleteRole failed: {str(error)}")
    click.echo("DeleteRole success")
