# -*- coding: utf-8 -*-


# test methods
def test_delete_first_record(app):
    app.session.login(username="admin", password="secret")
    app.record.delete_first()
    app.session.logout()
