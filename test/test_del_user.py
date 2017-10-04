from model.user import User


def test_delete_user(app):
    if app.user.count() == 0:
        app.user.create(
            User(name="new", surname="new", email="new", mobile="new", phone="new", company="new", address="new",
                 middle="new", nickname="new"))
    old_users = app.user.get_user_list()
    app.user.delete()
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    del old_users[0]
    assert old_users == new_users
