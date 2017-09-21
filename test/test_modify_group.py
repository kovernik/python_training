from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="name1", header="header1", footer="footer1"))
    app.session.logout()
