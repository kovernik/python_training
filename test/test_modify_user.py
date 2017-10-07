from model.user import User
from random import randrange


def test_modify_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="Mikhail"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user = User(firstname="new_name1")
    user.id = old_users[index].id
    app.user.modify_user_by_index(index, user)
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
