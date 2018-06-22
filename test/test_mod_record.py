# -*- coding: utf-8 -*-


# test methods
def test_modify_first_record(app):
    app.session.login(username="admin", password="secret")
    app.record.modify_first(field='firstname',
                            value='modified')
    app.record.modify_first(field='lastname',
                            value='modified')
    app.session.logout()
