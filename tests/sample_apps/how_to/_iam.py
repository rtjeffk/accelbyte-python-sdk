import time
from random import randint
from typing import Optional

from ._integration_test_case import IntegrationTestCase

from accelbyte_py_sdk.api.iam.models import ModelUserCreateRequest


class IAMTestCase(IntegrationTestCase):

    user_id: Optional[str] = None
    scope: str = "commerce account social publishing analytics"
    model_user_create_request = ModelUserCreateRequest.create(
        auth_type="EMAILPASSWD",
        country="US",
        display_name="testPythonServerSDKUser",
        login_id="",
        password="q!w@e#r$azsxdcfv"
    )

    # noinspection PyMethodMayBeStatic
    def do_create_user(self, body: ModelUserCreateRequest):
        # pylint: disable=no-self-use
        from accelbyte_py_sdk.api.iam import create_user

        body.login_id = f"testPythonServerSDKUser+{str(randint(0, 10_000)).rjust(5, '0')}@test.com"
        result, error = create_user(body=body)

        user_id: Optional[str] = None

        if error is None:
            user_id = result.user_id
        else:
            user_id = None

        return result, error, user_id

    def tearDown(self) -> None:
        from accelbyte_py_sdk.api.iam import delete_user

        if self.user_id is not None:
            _, error = delete_user(user_id=self.user_id)
            self.log_warning(msg=f"Failed to tear down user. {str(error)}", condition=error is not None)
            self.user_id = None
        super().tearDown()

    def test_create_user(self):
        # arrange
        # NOTE(elmer): can't delete, need user id

        # act
        _, error, user_id = self.do_create_user(body=self.model_user_create_request)
        self.user_id = user_id

        # assert
        self.assertIsNone(error, error)

    def test_delete_user(self):
        from accelbyte_py_sdk.api.iam import delete_user

        # arrange
        _, error, user_id = self.do_create_user(body=self.model_user_create_request)
        self.log_warning(msg=f"Failed to set up user. {str(error)}", condition=error is not None)
        self.user_id = user_id

        # act
        _, error = delete_user(user_id=self.user_id)

        # assert
        self.assertIsNone(error, error)
        self.user_id = None

    def test_get_user_by_user_id(self):
        from accelbyte_py_sdk.api.iam import get_user_by_user_id

        # arrange
        _, error, user_id = self.do_create_user(body=self.model_user_create_request)
        self.log_warning(msg=f"Failed to set up user. {str(error)}", condition=error is not None)
        self.user_id = user_id

        # act
        _, error = get_user_by_user_id(user_id=self.user_id)

        # assert
        self.assertIsNone(error, error)

    def test_update_user(self):
        from accelbyte_py_sdk.api.iam import update_user
        from accelbyte_py_sdk.api.iam.models import ModelUserResponse
        from accelbyte_py_sdk.api.iam.models import ModelUserUpdateRequest

        # arrange
        # add delay
        time.sleep(3)

        _, error, user_id = self.do_create_user(body=self.model_user_create_request)
        self.log_warning(msg=f"Failed to set up user. {str(error)}", condition=error is not None)
        self.user_id = user_id

        # act
        result, error = update_user(
            body=ModelUserUpdateRequest.create(country="ID"),
            user_id=self.user_id
        )

        # assert
        self.assertIsNone(error, error)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ModelUserResponse)
        self.assertEqual(result.country, "ID")

    def test_token_grant_v3(self):
        from accelbyte_py_sdk.api.iam import authorize_v3
        from accelbyte_py_sdk.api.iam import token_grant_v3
        from accelbyte_py_sdk.api.iam import user_authentication_v3
        from accelbyte_py_sdk.core import create_pkce_verifier_and_challenge_s256
        from accelbyte_py_sdk.core import get_client_id
        from accelbyte_py_sdk.core import get_env_user_credentials

        # arrange
        client_id, error = get_client_id()
        self.assertIsNone(error, error)

        code_verifier, code_challenge, code_challenge_method = create_pkce_verifier_and_challenge_s256()

        request_id, error = authorize_v3(
            response_type="code",
            client_id=client_id,
            scope=self.scope,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method
        )
        self.assertIsNone(error, error)
        self.assertIsNotNone(request_id)

        username, password = get_env_user_credentials()

        code, error = user_authentication_v3(
            user_name=username,
            password=password,
            request_id=request_id,
            client_id=client_id
        )
        self.assertIsNone(error, error)
        self.assertIsNotNone(code)

        # act
        _, error = token_grant_v3(
            grant_type="authorization_code",
            code=code,
            code_verifier=code_verifier,
            redirect_uri=""
        )

        # assert
        self.assertIsNone(error, error)

    def test_user_authentication_v3(self):
        from accelbyte_py_sdk.api.iam import authorize_v3
        from accelbyte_py_sdk.api.iam import user_authentication_v3
        from accelbyte_py_sdk.core import create_pkce_verifier_and_challenge_s256
        from accelbyte_py_sdk.core import get_client_id
        from accelbyte_py_sdk.core import get_env_user_credentials

        # arrange
        client_id, error = get_client_id()
        self.assertIsNone(error, error)

        code_verifier, code_challenge, code_challenge_method = create_pkce_verifier_and_challenge_s256()

        request_id, error = authorize_v3(
            response_type="code",
            client_id=client_id,
            scope=self.scope,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method
        )
        self.assertIsNone(error, error)
        self.assertIsNotNone(request_id)

        username, password = get_env_user_credentials()

        # act
        _, error = user_authentication_v3(
            user_name=username,
            password=password,
            request_id=request_id,
            client_id=client_id
        )

        # assert
        self.assertIsNone(error, error)

    def test_authorize_v3(self):
        from accelbyte_py_sdk.api.iam import authorize_v3
        from accelbyte_py_sdk.core import create_pkce_verifier_and_challenge_s256
        from accelbyte_py_sdk.core import get_client_id

        # arrange
        client_id, error = get_client_id()
        self.assertIsNone(error, error)

        code_verifier, code_challenge, code_challenge_method = create_pkce_verifier_and_challenge_s256()

        # act
        _, error = authorize_v3(
            response_type="code",
            client_id=client_id,
            scope=self.scope,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method
        )

        # assert
        self.assertIsNone(error, error)

    def test_login_client(self):
        from accelbyte_py_sdk.core import get_client_auth
        from accelbyte_py_sdk.services.auth import login_client

        # arrange
        client_auth, error = get_client_auth()
        self.assertIsNone(error, error)

        client_id, client_secret = client_auth

        # act
        _, error = login_client(client_id=client_id, client_secret=client_secret)

        # assert
        self.assertIsNone(error, error)

    def test_login_user(self):
        from accelbyte_py_sdk.core import get_env_user_credentials
        from accelbyte_py_sdk.services.auth import login_user

        # arrange
        username, password = get_env_user_credentials()

        # act
        _, error = login_user(username=username, password=password)

        # assert
        self.assertIsNone(error, error)

    def test_logout(self):
        from accelbyte_py_sdk.core import get_env_user_credentials
        from accelbyte_py_sdk.services.auth import login_user
        from accelbyte_py_sdk.services.auth import logout

        # arrange
        username, password = get_env_user_credentials()

        _, error = login_user(username=username, password=password)
        self.assertIsNone(error, error)

        # act
        _, error = logout()

        # assert
        self.assertIsNone(error, error)
