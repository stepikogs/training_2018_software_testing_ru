# -*- coding: utf-8 -*-


# test methods
def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(field='group_name',
                           value='modified_name')
    app.session.logout()
