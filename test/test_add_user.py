from model.user import User


def test_add_user(app):
    old_user = app.user.get_user_list()
    user = User(name="Name", surname="Last name", email="kovernik@softbalance.ru", mobile="+79110000000",
                phone="+78120001110", company="SoftBalance", address="Shaumyana, 55", middle="Middle",
                nickname="nickname")
    app.user.create(user)
    new_user = app.user.get_user_list()
    assert len(old_user) + 1 == len(new_user)
    old_user.append(user)
    assert sorted(new_user, key=User.id_or_max) == sorted(old_user, key=User.id_or_max)

