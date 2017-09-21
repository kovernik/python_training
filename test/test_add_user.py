from user import User


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.create(User(name="Name", surname="Last name", email="kovernik@softbalance.ru", mobile="+79110000000",
                         phone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                         nickname="nickname"))
    app.session.logout()


def test_add_empty_user(app):
    app.session.login(username="admin", password="secret")
    app.user.create(User(name="", surname="", email="", mobile="", phone="", company="", address="", middle="",
                         nickname=""))
    app.session.logout()
