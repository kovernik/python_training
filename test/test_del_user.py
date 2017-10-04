from model.user import User


def test_delete_user(app):
    if app.user.count() == 0:
        app.user.create(
            User(name="new", surname="new", email="new", mobile="new", phone="new", company="new", address="new",
                 middle="new", nickname="new"))
    old_users = app.user.get_user_list()
<<<<<<< HEAD
    app.user.delete()
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    del old_users[0]
=======
    app.user.test_delete_user()
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[0:1] = []
>>>>>>> c8e04c222356b95426d33d47a7b22fd59ac42272
    assert old_users == new_users
