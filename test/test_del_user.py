from model.user import User


def test_delete_user(app):
    if app.user.count() == 0:
        app.user.create(
            User(name="new", surname="new", email="new", mobile="new", phone="new", company="new", address="new",
                 middle="new", nickname="new"))
    app.user.delete()
