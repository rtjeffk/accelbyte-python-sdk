# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import json
import logging
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Callable, IO, Optional, Tuple, Union

import httpx
import requests

from ._header import Header
from ._http_response import HttpResponse
from ._operation import Operation
from ._utils import create_curl_request

_LOGGER = logging.getLogger("accelbyte_py_sdk.http")

# NOTE(elmer): convert into a class if needed
HttpRawResponse = Tuple[int, str, Any]  # code, content-type, content


class HttpClient(ABC):

    request_log_formatter: Optional[Callable[[dict], str]] = None
    response_log_formatter: Optional[Callable[[dict], str]] = None

    # noinspection PyMethodMayBeStatic
    def is_async_compatible(self) -> bool:
        return False

    @abstractmethod
    def create_request(
            self,
            operation: Operation,
            base_url: Union[None, str] = None,
            headers: Union[None, Header] = None,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        pass

    @abstractmethod
    def send_request(
            self,
            request: Any,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        pass

    async def send_request_async(
            self,
            request: Any,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        if not self.is_async_compatible():
            return None, HttpResponse.create_error(400, "HTTP client is not async compatible.")
        raise NotImplementedError

    @abstractmethod
    def handle_response(
            self,
            raw_response: Any,
            **kwargs
    ) -> Tuple[Union[None, HttpRawResponse], Union[None, HttpResponse]]:
        pass

    def run_request(
            self,
            operation: Operation,
            base_url: Union[None, str] = None,
            headers: Union[None, Header] = None,
            **kwargs
    ) -> Tuple[Union[None, HttpRawResponse], Union[None, HttpResponse]]:
        request, error = self.create_request(operation, base_url, headers, **kwargs)
        if error:
            return None, error

        raw_response, error = self.send_request(request, **kwargs)
        if error:
            return None, error

        response, error = self.handle_response(raw_response, **kwargs)
        if error:
            return None, error

        return response, None

    def _log_request(self, request_dict: dict) -> None:
        req_fmt = self.request_log_formatter or format_request_log
        _LOGGER.debug(req_fmt(request_dict))

    def _log_response(self, response_dict: dict):
        res_fmt = self.response_log_formatter or format_response_log
        _LOGGER.debug(res_fmt(response_dict))


# TODO(elmer): move to a separate file once it gets too big
class RequestsHttpClient(HttpClient):

    def __init__(self, allow_redirects: bool = True):
        self.allow_redirects = allow_redirects
        self.session = requests.Session()

    def create_request(
            self,
            operation: Operation,
            base_url: Union[None, str] = None,
            headers: Union[None, Header] = None,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        method, url, headers, files, data, json_ = convert_operation(operation, base_url, headers)
        prepared_request = requests.Request(
            method=method,
            url=url,
            headers=headers,
            files=files,
            data=data,
            json=json_,
        ).prepare()

        return prepared_request, None

    def send_request(
            self,
            request: Any,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        if "allow_redirects" not in kwargs:
            kwargs["allow_redirects"] = self.allow_redirects
        self.log_request(request)
        try:
            raw_response = self.session.send(request, **kwargs)
        except requests.exceptions.ConnectionError as e:
            _LOGGER.error(str(e))
            return None, HttpResponse.create_connection_error()
        return raw_response, None

    def handle_response(
            self,
            raw_response: requests.Response,
            **kwargs
    ) -> Tuple[Union[None, HttpRawResponse], Union[None, HttpResponse]]:
        status_code = raw_response.status_code
        if 400 <= status_code <= 599:
            _LOGGER.error(f"[{status_code}] {raw_response.text}")

        if status_code == 201:
            content_type = "location"
            content = raw_response.headers.get("location", "")
        elif raw_response.is_redirect:
            content_type = "location"
            content = raw_response.headers["location"]
        elif raw_response.history:
            content_type = "location"
            content = None
            history = next(filter(lambda h: "location" in h.headers, raw_response.history))
            if history:
                status_code = history.status_code
                content = history.headers["location"]
            if content is None:
                return None, HttpResponse.create_unhandled_error()
        elif "Content-Type" in raw_response.headers:
            content_type = raw_response.headers["Content-Type"]
            if is_json_mime_type(content_type):
                try:
                    content = raw_response.json()
                    if content is None:
                        _LOGGER.warning(f"Expecting 'application/json' content received null.")
                        content = ""
                except ValueError:
                    content = ""
            elif content_type.startswith("text/"):
                content = raw_response.text
                if content is None:
                    _LOGGER.warning(f"Expecting 'text/*' content received null.")
                    content = ""
            else:
                content = raw_response.raw.data
        else:
            content_type = None
            content = None

        self.log_response(raw_response)

        return (status_code, content_type, content), None

    def log_request(self, prepared_request: requests.PreparedRequest) -> None:
        if _LOGGER.isEnabledFor(logging.DEBUG):
            request_dict = RequestsHttpClient.convert_request_to_dict(prepared_request)
            request_dict["timestamp"] = int(time.time())
            self._log_request(request_dict)

    def log_response(self, response: requests.Response) -> None:
        if _LOGGER.isEnabledFor(logging.DEBUG):
            response_dict = RequestsHttpClient.convert_response_to_dict(response)
            response_dict["timestamp"] = int(time.time())
            self._log_response(response_dict)

    @staticmethod
    def convert_to_curl(prepared_request: requests.PreparedRequest) -> str:
        return create_curl_request(
            uri=prepared_request.url,
            method=prepared_request.method,
            headers={k: v for k, v in prepared_request.headers.items()},
            data=prepared_request.body
        )

    @staticmethod
    def convert_request_to_dict(prepared_request: requests.PreparedRequest) -> dict:
        return {
            "url": prepared_request.url,
            "method": prepared_request.method,
            "headers": {k: v for k, v in prepared_request.headers.items()},
            "data": prepared_request.body
        }

    @staticmethod
    def convert_response_to_dict(response: requests.Response) -> dict:
        return {
            "url": response.url,
            "status_code": response.status_code,
            "elapsed": response.elapsed.total_seconds(),
            "headers": {k: v for k, v in response.headers.items()},
            "body": response.content,
        }


class HttpxHttpClient(HttpClient):

    def __init__(
            self,
            max_connections: int = 100,
            max_keepalive_connections: int = 20,
    ):
        limits = httpx.Limits(
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
        )
        self.transport = httpx.HTTPTransport(
            verify=True,
            cert=None,
            http1=True,
            http2=True,
            limits=limits,
            trust_env=True,
        )
        self.transport_async = httpx.AsyncHTTPTransport(
            verify=True,
            cert=None,
            http1=True,
            http2=False,
            limits=limits,
            trust_env=True,
        )
        self.client = httpx.Client(transport=self.transport)
        self.client_async = httpx.AsyncClient(transport=self.transport_async)

    # noinspection PyMethodMayBeStatic
    def is_async_compatible(self) -> bool:
        return True

    def create_request(
            self,
            operation: Operation,
            base_url: Union[None, str] = None,
            headers: Union[None, Header] = None,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:

        method, url, headers, files, data, json_ = convert_operation(operation, base_url, headers)

        httpx_request = httpx.Request(
            method=method,
            url=url,
            headers=headers,
            files=files,
            data=data,
            json=json_,
        )

        return httpx_request, None

    def send_request(
            self,
            request: Any,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        self.log_request(request)
        return self.client.send(request), None

    async def send_request_async(
            self,
            request: Any,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        self.log_request(request)
        return await self.client_async.send(request), None

    def handle_response(
            self,
            raw_response: httpx.Response,
            **kwargs
    ) -> Tuple[Union[None, HttpRawResponse], Union[None, HttpResponse]]:
        status_code = raw_response.status_code
        if 400 <= status_code <= 599:
            _LOGGER.error(f"[{status_code}] {raw_response.text}")

        if raw_response.is_redirect:
            content_type = "location"
            content = raw_response.headers["location"]
        elif raw_response.history:
            content_type = "location"
            content = None
            history = next(filter(lambda h: "location" in h.headers, raw_response.history))
            if history:
                status_code = history.status_code
                content = history.headers["location"]
            if content is None:
                return None, HttpResponse.create_unhandled_error()
        elif "Content-Type" in raw_response.headers:
            content_type = raw_response.headers["Content-Type"]
            if is_json_mime_type(content_type):
                try:
                    content = raw_response.json()
                    if content is None:
                        _LOGGER.warning(f"Expecting 'application/json' content received null.")
                        content = ""
                except ValueError:
                    content = ""
            elif content_type.startswith("text/"):
                content = raw_response.text
                if content is None:
                    _LOGGER.warning(f"Expecting 'text/*' content received null.")
                    content = ""
            else:
                return None, HttpResponse.create_unhandled_error()
        else:
            content_type = None
            content = None

        self.log_response(raw_response)

        return (status_code, content_type, content), None

    def log_request(self, httpx_request: httpx.Request) -> None:
        if _LOGGER.isEnabledFor(logging.DEBUG):
            request_dict = HttpxHttpClient.convert_request_to_dict(httpx_request)
            request_dict["timestamp"] = int(time.time())
            self._log_request(request_dict)

    def log_response(self, httpx_response: httpx.Response) -> None:
        if _LOGGER.isEnabledFor(logging.DEBUG):
            response_dict = HttpxHttpClient.convert_response_to_dict(httpx_response)
            response_dict["timestamp"] = int(time.time())
            self._log_request(response_dict)

    @staticmethod
    def convert_to_curl(httpx_request: httpx.Request) -> str:
        return create_curl_request(
            uri=httpx_request.url,
            method=httpx_request.method,
            headers={k: v for k, v in httpx_request.headers.items()},
            data=httpx_request.content
        )

    @staticmethod
    def convert_request_to_dict(httpx_request: httpx.Request) -> dict:
        return {
            "url": httpx_request.url,
            "method": httpx_request.method,
            "headers": {k: v for k, v in httpx_request.headers.items()},
            "data": httpx_request.content,
        }

    @staticmethod
    def convert_response_to_dict(httpx_response: httpx.Response) -> dict:
        return {
            "url": httpx_response.url,
            "status_code": httpx_response.status_code,
            "elapsed": httpx_response.elapsed.total_seconds(),
            "headers": {k: v for k, v in httpx_response.headers.items()},
            "body": httpx_response.content,
        }


# TODO(elmer): convert into a dataclass?
def convert_operation(
        operation: Operation,
        base_url: Union[None, str] = None,
        headers: Union[None, Header] = None,
) -> Tuple[
    str,     # method
    str,     # url
    Header,  # headers
    Any,     # files
    Any,     # data
    Any,     # json
]:
    if not operation.is_valid():
        raise Exception("Missing required values.")

    headers = headers if headers is not None else operation.get_headers()

    body_params = operation.get_body_params()
    form_data_params = operation.get_form_data_params()

    content_type = headers.get("Content-Type")

    if body_params is not None:
        if is_json_mime_type(content_type):
            files, data, json_ = None, None, body_params
        else:
            files, data, json_ = None, json.dumps(body_params), None
    elif form_data_params:
        preprocess_form_data_params(form_data_params)
        files = {}
        data = {}
        json_ = None
        for k, v in form_data_params.items():
            if is_file(k):
                files[k] = v
            else:
                data[k] = v
        if not files:
            files = None
        if not data:
            data = None
    else:
        files = None
        data = None
        json_ = None

    # NOTE(elmer): Remove 'Content-Type' when 'files' is truthy.
    # See: https://stackoverflow.com/questions/12385179/how-to-send-a-multipart-form-data-with-requests-in-python#comment90642370_12385661
    if files and "Content-Type" in headers:
        headers.pop("Content-Type")

    return operation.method, operation.get_full_url(base_url=base_url), headers, files, data, json_


def convert_any_to_file_tuple(name: str, file: Any) -> Tuple[str, IO]:
    if isinstance(file, IO):
        return name, file

    if isinstance(file, str):
        file = Path(file)
    if isinstance(file, Path):
        if not file.exists():
            raise FileNotFoundError
        return file.name, file.open()

    raise ValueError


def format_request_log(request_dict: dict) -> str:
    return str(request_dict)


def format_response_log(response_dict: dict) -> str:
    return str(response_dict)


def is_file(key: str) -> bool:
    return key.casefold() == "file"


def is_json_mime_type(mime_type: Optional[str]) -> bool:
    if mime_type is None:
        return False
    split = mime_type.split("/")
    if len(split) != 2:
        _LOGGER.warning(f"Invalid MIME Type: {mime_type}")
        return False
    main, sub = split
    return main == "application" and (sub == "json" or sub.endswith("+json"))


def preprocess_form_data_params(form_data_params: dict) -> None:
    for form_data_key in form_data_params.keys():
        if is_file(form_data_key):
            form_data_params[form_data_key] = convert_any_to_file_tuple(form_data_key, form_data_params[form_data_key])
