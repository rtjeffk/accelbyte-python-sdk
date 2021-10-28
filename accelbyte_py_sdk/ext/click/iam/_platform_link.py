import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import platform_link as platform_link_internal


@click.command()
@click.argument("ticket", type=str)
@click.argument("user_id", type=str)
@click.argument("platform_id", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def platform_link(
        ticket: str,
        user_id: str,
        platform_id: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(platform_link_internal.__doc__)
    result, error = platform_link_internal(
        ticket=ticket,
        user_id=user_id,
        platform_id=platform_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"PlatformLink failed: {str(error)}")
    click.echo("PlatformLink success")
