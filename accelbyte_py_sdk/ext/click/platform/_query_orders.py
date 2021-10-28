import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import query_orders as query_orders_internal
from ....api.platform.models import OrderPagingResult
from ....api.platform.models import ValidationErrorEntity


@click.command()
@click.option("--status", "status", type=str)
@click.option("--order_nos", "order_nos", type=str)
@click.option("--start_time", "start_time", type=str)
@click.option("--end_time", "end_time", type=str)
@click.option("--offset", "offset", type=int)
@click.option("--limit", "limit", type=int)
@click.option("--sort_by", "sort_by", type=str)
@click.option("--with_total", "with_total", type=bool)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def query_orders(
        status: Optional[str] = None,
        order_nos: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_by: Optional[str] = None,
        with_total: Optional[bool] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(query_orders_internal.__doc__)
    try:
        order_nos_json = json.loads(order_nos)
        order_nos = [str.create_from_dict(i0) for i0 in order_nos_json]
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'orderNos'. {str(e)}")
    result, error = query_orders_internal(
        status=status,
        order_nos=order_nos,
        start_time=start_time,
        end_time=end_time,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        with_total=with_total,
        namespace=namespace,
    )
    if error:
        raise Exception(f"queryOrders failed: {str(error)}")
    click.echo("queryOrders success")