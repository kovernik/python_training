from model.user import User
from random import randrange


def test_delete_some_user(app):
    if app.user.count() == 0:
        app.user.create(
            User(name="Name", surname="Last name", email="kovernik@softbalance.ru", mobilephone="+79110000000",
                 homephone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                 nickname="nickname"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    del old_users[index]
    assert old_users == new_users
