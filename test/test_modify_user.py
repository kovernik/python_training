from model.user import User


def test_modify_user(app):
    if app.user.count() == 0:
        app.user.create(
            User(name="new", surname="new", email="new", mobile="new", phone="new", company="new", address="new",
                 middle="new", nickname="new"))
    app.user.modify(
        User(name="new1", surname="new1", email="new1", mobile="new1", phone="new1", company="new1", address="new1",
             middle="new1", nickname="new1"))
