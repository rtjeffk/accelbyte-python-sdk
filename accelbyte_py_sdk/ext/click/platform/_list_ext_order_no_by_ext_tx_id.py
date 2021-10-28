import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import list_ext_order_no_by_ext_tx_id as list_ext_order_no_by_ext_tx_id_internal


@click.command()
@click.argument("ext_tx_id", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def list_ext_order_no_by_ext_tx_id(
        ext_tx_id: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(list_ext_order_no_by_ext_tx_id_internal.__doc__)
    result, error = list_ext_order_no_by_ext_tx_id_internal(
        ext_tx_id=ext_tx_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"listExtOrderNoByExtTxId failed: {str(error)}")
    click.echo("listExtOrderNoByExtTxId success")