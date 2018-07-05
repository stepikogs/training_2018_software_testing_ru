# -*- coding: utf-8 -*-
from model.group import Group


# test methods
def test_modify_first_group(app):
    app.group.provide()
    old_groups = app.group.get_list()
    app.group.modify_first(Group(group_name='modified_name'))
    new_groups = app.group.get_list()
    assert len(old_groups) == len(new_groups)
