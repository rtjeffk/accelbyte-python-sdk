import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import fulfill_user_order as fulfill_user_order_internal
from ....api.platform.models import ErrorEntity
from ....api.platform.models import OrderInfo


@click.command()
@click.argument("user_id", type=str)
@click.argument("order_no", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def fulfill_user_order(
        user_id: str,
        order_no: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(fulfill_user_order_internal.__doc__)
    result, error = fulfill_user_order_internal(
        user_id=user_id,
        order_no=order_no,
        namespace=namespace,
    )
    if error:
        raise Exception(f"fulfillUserOrder failed: {str(error)}")
    click.echo("fulfillUserOrder success")