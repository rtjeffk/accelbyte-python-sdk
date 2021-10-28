import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import get_google_iap_config as get_google_iap_config_internal
from ....api.platform.models import GoogleIAPConfigInfo


@click.command()
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def get_google_iap_config(
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(get_google_iap_config_internal.__doc__)
    result, error = get_google_iap_config_internal(
        namespace=namespace,
    )
    if error:
        raise Exception(f"getGoogleIAPConfig failed: {str(error)}")
    click.echo("getGoogleIAPConfig success")