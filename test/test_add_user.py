from user import User


def test_add_user(app_user):
    app_user.session.login(username="admin", password="secret")
    app_user.user.create(User(name="Name", surname="Last name", email="kovernik@softbalance.ru", mobile="+79110000000",
                         phone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                         nickname="nickname"))
    app_user.session.logout()


def test_add_empty_user(app_user):
    app_user.session.login(username="admin", password="secret")
    app_user.user.create(User(name="", surname="", email="", mobile="", phone="", company="", address="", middle="",
                         nickname=""))
    app_user.session.logout()
