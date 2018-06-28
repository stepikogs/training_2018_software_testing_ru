# -*- coding: utf-8 -*-
from model.group import Group


# test methods
def test_modify_first_group(app):
    app.group.modify_first(Group(group_name='modified_name'))
