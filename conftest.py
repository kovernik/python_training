import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
<<<<<<< HEAD
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
=======
    fixture = Application()
    fixture.session.login(username="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()

>>>>>>> 379862cfbe3f982f0bcce2346d6dd7c93debd0f7
    request.addfinalizer(fin)
    return fixture
