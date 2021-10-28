import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.iam import platform_unlink as platform_unlink_internal


@click.command()
@click.argument("user_id", type=str)
@click.argument("platform_id", type=str)
@click.option("--platform_namespace", "platform_namespace", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def platform_unlink(
        user_id: str,
        platform_id: str,
        platform_namespace: Optional[str] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(platform_unlink_internal.__doc__)
    result, error = platform_unlink_internal(
        user_id=user_id,
        platform_id=platform_id,
        platform_namespace=platform_namespace,
        namespace=namespace,
    )
    if error:
        raise Exception(f"PlatformUnlink failed: {str(error)}")
    click.echo("PlatformUnlink success")