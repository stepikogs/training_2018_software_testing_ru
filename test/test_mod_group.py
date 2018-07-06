# -*- coding: utf-8 -*-
from model.group import Group


# test methods
def test_modify_first_group(app):
    app.group.provide()
    old_groups = app.group.get_list()
    group = Group(group_name='modified_name')
    group.id = old_groups[0].id
    app.group.modify_first(group)
    new_groups = app.group.get_list()
    print(new_groups[0].group_name)
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
