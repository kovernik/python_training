import pytest
from fixture.application import Application
from fixture.user_application import User_application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope="session")
def app_user(request):
    fixture = User_application()
    request.addfinalizer(fixture.destroy)
    return fixture
