def test_delete_user(app):
    app.session.login(username="admin", password="secret")
    app.user.delete()
    app.session.logout()
