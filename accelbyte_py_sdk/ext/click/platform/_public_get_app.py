import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import public_get_app as public_get_app_internal
from ....api.platform.models import AppInfo
from ....api.platform.models import ErrorEntity


@click.command()
@click.argument("item_id", type=str)
@click.option("--store_id", "store_id", type=str)
@click.option("--region", "region", type=str)
@click.option("--language", "language", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def public_get_app(
        item_id: str,
        store_id: Optional[str] = None,
        region: Optional[str] = None,
        language: Optional[str] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(public_get_app_internal.__doc__)
    result, error = public_get_app_internal(
        item_id=item_id,
        store_id=store_id,
        region=region,
        language=language,
        namespace=namespace,
    )
    if error:
        raise Exception(f"publicGetApp failed: {str(error)}")
    click.echo("publicGetApp success")