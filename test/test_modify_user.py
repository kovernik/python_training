from model.user import User


def test_modify_user(app):
    if app.user.count() == 0:
        app.user.create(User(name="Mikhail"))
    old_user = app.user.get_user_list()
    user = User(name="new_name1")
    user.id = old_user[0].id
    app.user.modify(user)
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)
    old_user[0] = user
    assert sorted(old_user, key=User.id_or_max) == sorted(new_user, key=User.id_or_max)
