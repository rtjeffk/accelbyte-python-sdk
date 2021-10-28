import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import decrease_ticket_sale as decrease_ticket_sale_internal
from ....api.platform.models import ErrorEntity
from ....api.platform.models import TicketSaleDecrementRequest
from ....api.platform.models import ValidationErrorEntity


@click.command()
@click.argument("booth_name", type=str)
@click.option("--body", "body", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def decrease_ticket_sale(
        booth_name: str,
        body: Optional[str] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(decrease_ticket_sale_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = TicketSaleDecrementRequest.create_from_dict(body_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = decrease_ticket_sale_internal(
        booth_name=booth_name,
        body=body,
        namespace=namespace,
    )
    if error:
        raise Exception(f"decreaseTicketSale failed: {str(error)}")
    click.echo("decreaseTicketSale success")