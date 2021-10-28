import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.platform import test_ali_pay_config as test_ali_pay_config_internal
from ....api.platform.models import AliPayConfig
from ....api.platform.models import TestResult


@click.command()
@click.option("--body", "body", type=str)
@click.option("--sandbox", "sandbox", type=bool)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def test_ali_pay_config(
        body: Optional[str] = None,
        sandbox: Optional[bool] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(test_ali_pay_config_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = AliPayConfig.create_from_dict(body_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = test_ali_pay_config_internal(
        body=body,
        sandbox=sandbox,
    )
    if error:
        raise Exception(f"testAliPayConfig failed: {str(error)}")
    click.echo("testAliPayConfig success")