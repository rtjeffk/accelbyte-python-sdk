import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import get_item_id_by_sku as get_item_id_by_sku_internal
from ....api.platform.models import ErrorEntity
from ....api.platform.models import ItemId


@click.command()
@click.argument("sku", type=str)
@click.option("--store_id", "store_id", type=str)
@click.option("--active_only", "active_only", type=bool)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def get_item_id_by_sku(
        sku: str,
        store_id: Optional[str] = None,
        active_only: Optional[bool] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(get_item_id_by_sku_internal.__doc__)
    result, error = get_item_id_by_sku_internal(
        sku=sku,
        store_id=store_id,
        active_only=active_only,
        namespace=namespace,
    )
    if error:
        raise Exception(f"getItemIdBySku failed: {str(error)}")
    click.echo("getItemIdBySku success")