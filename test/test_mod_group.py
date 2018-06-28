# -*- coding: utf-8 -*-
from model.group import Group


# test methods
def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(group_name='modified_name'))
    app.session.logout()
