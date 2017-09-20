from user import User
from user_application import User_application
import pytest


@pytest.fixture
def app(request):
    fixture = User_application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.login(username="admin", password="secret")
    app.create_user(User(name="Name", surname="Last name", email="kovernik@softbalance.ru", mobile="+79110000000",
                         phone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                         nickname="nickname"))
    app.logout()


def test_add_empty_user(app):
    app.login(username="admin", password="secret")
    app.create_user(User(name="", surname="", email="", mobile="", phone="", company="", address="", middle="",
                         nickname=""))
    app.logout()
