from model.user import User


def test_add_user(app):
    old_user = app.user.get_user_list()
    user = User(firstname="Name", lastname="Last name", email="kovernik@softbalance.ru", mobilephone="+79110000000",
                homephone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                nickname="nickname")
    app.user.create(user)
    assert len(old_user) + 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user.append(user)
    assert sorted(new_user, key=User.id_or_max) == sorted(old_user, key=User.id_or_max)
