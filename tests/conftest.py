import pytest
from rest_framework.test import APIClient
from tests.factories.user_factory import UserFactory
from users.models import UserAccount
@pytest.fixture
def user() -> UserAccount:
    return UserFactory()

@pytest.fixture
def user_with_no_name() -> UserAccount:
    return UserFactory(first_name=None, last_name=None, age=None)

@pytest.fixture
def api_client() -> APIClient:
    return APIClient()