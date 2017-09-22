from model.user import User


def test_add_user(app):
    app.user.create(User(name="Name", surname="Last name", email="kovernik@softbalance.ru", mobile="+79110000000",
                         phone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                         nickname="nickname"))


def test_add_empty_user(app):
    app.user.create(User(name="", surname="", email="", mobile="", phone="", company="", address="", middle="",
                         nickname=""))
