# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import get_namespace as get_services_namespace
from ....core import run_request
from ....core import same_doc_as

from ..models import ErrorEntity
from ..models import TicketAcquireRequest
from ..models import TicketAcquireResult
from ..models import TicketBoothID
from ..models import TicketDynamicInfo
from ..models import TicketSaleDecrementRequest
from ..models import TicketSaleIncrementRequest
from ..models import TicketSaleIncrementResult
from ..models import ValidationErrorEntity

from ..operations.ticket import AcquireUserTicket
from ..operations.ticket import DecreaseTicketSale
from ..operations.ticket import GetTicketBoothID
from ..operations.ticket import GetTicketDynamic
from ..operations.ticket import IncreaseTicketSale


@same_doc_as(AcquireUserTicket)
def acquire_user_ticket(user_id: str, booth_name: str, body: Optional[TicketAcquireRequest] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AcquireUserTicket.create(
        user_id=user_id,
        booth_name=booth_name,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DecreaseTicketSale)
def decrease_ticket_sale(booth_name: str, body: Optional[TicketSaleDecrementRequest] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DecreaseTicketSale.create(
        booth_name=booth_name,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetTicketBoothID)
def get_ticket_booth_id(booth_name: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetTicketBoothID.create(
        booth_name=booth_name,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetTicketDynamic)
def get_ticket_dynamic(booth_name: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetTicketDynamic.create(
        booth_name=booth_name,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(IncreaseTicketSale)
def increase_ticket_sale(booth_name: str, body: Optional[TicketSaleIncrementRequest] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = IncreaseTicketSale.create(
        booth_name=booth_name,
        body=body,
        namespace=namespace,
    )
    return run_request(request)