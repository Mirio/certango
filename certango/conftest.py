import pytest

from certango.users.models import User
from certango.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    # pylint: disable=unused-argument
    # 'db' used during the Factory class
    return UserFactory()
