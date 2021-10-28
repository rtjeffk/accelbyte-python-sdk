import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import delete_category as delete_category_internal
from ....api.platform.models import ErrorEntity
from ....api.platform.models import FullCategoryInfo


@click.command()
@click.argument("category_path", type=str)
@click.argument("store_id", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def delete_category(
        category_path: str,
        store_id: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(delete_category_internal.__doc__)
    result, error = delete_category_internal(
        category_path=category_path,
        store_id=store_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"deleteCategory failed: {str(error)}")
    click.echo("deleteCategory success")