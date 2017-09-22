from model.user import User


def test_modify_user(app):
    app.user.modify(User(name="Name1", surname="Last name1", email="kovernik@softbalance.ru1", mobile="+791100000001",
                         phone="+781200011101", company="SoftBalance1", address="Shaumyana, 551", middle="Middle1",
                         nickname="nickname1"))
